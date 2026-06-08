import numpy as np
from utils import plot_compare, plot_function

def f(t, y):
	return np.cos(3*t) * np.exp(-t) - y

def y(t):
    return (np.exp(-t) * np.sin(3*t)) / 3

def euler(f, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(a, b, N + 1)
    w = np.zeros(N + 1)
    
    w[0] = y0
    for i in range(N):
        w[i+1] = w[i] + h * f(t[i], w[i])
        
    return t, w

if __name__ == "__main__":
    y0 = 0
    a = 0.0
    b = 6.0
    N = 50

    t_i, w = euler(f, y0, a, b, N)
    # plot_function(t_i, w)

	# Comparar a solução aproximada com a solução exata
    t = np.linspace(a, b, 256)
    plot_compare(t, y(t), t_i, w, (b - a) / N, name="Método de Euler")
    
