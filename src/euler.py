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




