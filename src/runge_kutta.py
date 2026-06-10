"""Métodos de Runge-Kutta para PVIs escalares e sistemas.

A função f deve ter assinatura f(t, y), onde y é um escalar ou um
numpy.ndarray. O passo é fixo. As implementações são vetoriais, então
o mesmo código resolve uma EDO escalar ou um sistema (ex.: SIR).
"""

import numpy as np


def rk4(f, t0, y0, h, n):
    """Runge-Kutta clássico de 4ª ordem (erro global O(h^4)).

    Parameters
    ----------
    f : callable
        Lado direito do PVI, f(t, y) -> dy/dt. y pode ser escalar ou vetor.
    t0 : float
        Tempo inicial.
    y0 : float or array_like
        Condição inicial y(t0).
    h : float
        Tamanho do passo.
    n : int
        Número de passos.

    Returns
    -------
    t : ndarray, shape (n+1,)
        Malha de tempo.
    y : ndarray, shape (n+1, ...) 
        Aproximação da solução em cada ponto da malha.
    """
    y0 = np.atleast_1d(np.asarray(y0, dtype=float))
    t = t0 + h * np.arange(n + 1)
    y = np.empty((n + 1, y0.size), dtype=float)
    y[0] = y0

    for i in range(n):
        ti, yi = t[i], y[i]
        k1 = np.asarray(f(ti, yi), dtype=float)
        k2 = np.asarray(f(ti + h / 2, yi + h / 2 * k1), dtype=float)
        k3 = np.asarray(f(ti + h / 2, yi + h / 2 * k2), dtype=float)
        k4 = np.asarray(f(ti + h, yi + h * k3), dtype=float)
        y[i + 1] = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return t, np.squeeze(y)


def rk2_heun(f, t0, y0, h, n):
    """Runge-Kutta de 2ª ordem — método de Heun (erro global O(h^2)).

    Preditor por Euler, corretor pela média das inclinações nos extremos.
    """
    y0 = np.atleast_1d(np.asarray(y0, dtype=float))
    t = t0 + h * np.arange(n + 1)
    y = np.empty((n + 1, y0.size), dtype=float)
    y[0] = y0

    for i in range(n):
        ti, yi = t[i], y[i]
        k1 = np.asarray(f(ti, yi), dtype=float)
        k2 = np.asarray(f(ti + h, yi + h * k1), dtype=float)
        y[i + 1] = yi + (h / 2) * (k1 + k2)

    return t, np.squeeze(y)
