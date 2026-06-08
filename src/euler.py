import numpy as np
from utils import plot_compare4

def f(t, y):
    return y + 2 * np.exp(t) * np.cos(t)

def df(t, y):
    return f(t, y) + 2 * np.exp(t) * (np.cos(t) - np.sin(t))

def y(t):
    return np.exp(t) * (2 * np.sin(t) + 1)

def euler(f, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(a, b, N + 1)
    w = np.zeros(N + 1)
    
    w[0] = y0
    for i in range(N):
        w[i+1] = w[i] + h * f(t[i], w[i])
        
    return t, w

def taylor2(f, df, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(a, b, N + 1)
    w = np.zeros(N + 1)
    
    w[0] = y0
    for i in range(N):
        w[i+1] = w[i] + h * f(t[i], w[i]) + (h**2 / 2) * df(t[i], w[i])
        
    return t, w

def euler_melhorado(f, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(a, b, N + 1)
    w = np.zeros(N + 1)
    
    w[0] = y0
    for i in range(N):
        w[i+1] = w[i] + (h / 2.0) * (f(t[i], w[i]) + f(t[i+1], w[i] + h * f(t[i], w[i])))
        
    return t, w

if __name__ == "__main__":
    y0 = 1
    a = 0.0
    b = 2.5
    N = 12

    t_euler, w_euler = euler(f, y0, a, b, N)
    t_taylor, w_taylor = taylor2(f, df, y0, a, b, N)
    t_melhorado, w_melhorado = euler_melhorado(f, y0, a, b, N)
    # plot_function(t_i, w)

	# plotar soluções aproximadas vs a solução exata
    t = np.linspace(a, b, 256)
    plot_compare4(t, y(t), t_euler, w_euler, t_taylor, w_taylor, t_melhorado, w_melhorado, first_name="Solução Exata", second_name="Método de Euler", third_name="Método de Taylor 2ª Ordem", fourth_name="Método de Euler Melhorado")
    
