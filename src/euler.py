"""Métodos de Euler para PVIs escalares e sistemas.

f deve ter assinatura f(t, y); y escalar ou numpy.ndarray. Passo fixo.
"""

import numpy as np


def euler_explicit(f, t0, y0, h, n):
    """Euler explícito (forward), erro global O(h).

    Returns
    -------
    t : ndarray (n+1,)
    y : ndarray (n+1, ...)
    """
    y0 = np.atleast_1d(np.asarray(y0, dtype=float))
    t = t0 + h * np.arange(n + 1)
    y = np.empty((n + 1, y0.size), dtype=float)
    y[0] = y0

    for i in range(n):
        y[i + 1] = y[i] + h * np.asarray(f(t[i], y[i]), dtype=float)

    return t, np.squeeze(y)


def euler_implicit(f, t0, y0, h, n, tol=1e-10, max_iter=100):
    """Euler implícito (backward) por iteração de ponto fixo.

    Resolve y_{i+1} = y_i + h f(t_{i+1}, y_{i+1}) iterando o ponto fixo
    com chute inicial dado por um passo de Euler explícito. Estável para
    problemas stiff; aqui mantido escalar/vetorial simples.
    """
    y0 = np.atleast_1d(np.asarray(y0, dtype=float))
    t = t0 + h * np.arange(n + 1)
    y = np.empty((n + 1, y0.size), dtype=float)
    y[0] = y0

    for i in range(n):
        t_next = t[i + 1]
        guess = y[i] + h * np.asarray(f(t[i], y[i]), dtype=float)  # preditor
        for _ in range(max_iter):
            new = y[i] + h * np.asarray(f(t_next, guess), dtype=float)
            if np.linalg.norm(new - guess) < tol:
                guess = new
                break
            guess = new
        y[i + 1] = guess

    return t, np.squeeze(y)


# alias curto, conveniente nos notebooks
euler = euler_explicit
