"""Funções auxiliares: medidas de erro e plotagem."""

import numpy as np
import matplotlib.pyplot as plt


def max_abs_error(y_approx, y_ref):
    """Erro máximo absoluto (norma do sup) entre aproximação e referência."""
    return np.max(np.abs(np.asarray(y_approx) - np.asarray(y_ref)))


def global_error(t, y_approx, y_exact_func):
    """Erro global em cada ponto da malha, dada a solução exata y_exact_func(t)."""
    y_exact = np.array([y_exact_func(ti) for ti in t])
    return np.abs(np.asarray(y_approx) - y_exact)


def plot_solution(t, y, labels=None, title="", ylabel="y(t)", ax=None):
    """Plota uma ou mais componentes de y vs t.

    y pode ter shape (n+1,) ou (n+1, k). labels é uma lista de nomes
    para as k componentes.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    y = np.asarray(y)
    if y.ndim == 1:
        ax.plot(t, y, label=labels[0] if labels else None)
    else:
        for j in range(y.shape[1]):
            lab = labels[j] if labels else f"y[{j}]"
            ax.plot(t, y[:, j], label=lab)
    ax.set_xlabel("t")
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    if labels:
        ax.legend()
    ax.grid(True, alpha=0.3)
    return ax
