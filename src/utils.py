import matplotlib.pyplot as plt

def plot_function(t, y):
    plt.figure(figsize=(10, 6))

    plt.plot(t, y, label='Função', color='blue', linewidth=2)

    plt.title('Gráfico da Função', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()

def plot_compare(t, y, t_i, w, h, name="Método de Euler"):
    plt.figure(figsize=(10, 6))

    plt.plot(t, y, label='Solução Exata', color='blue', linewidth=2)

    plt.plot(t_i, w, label=f'{name} (h = {h})', 
             color='red', linestyle='--', marker='o', linewidth=1, markersize=5)

    plt.title(f'Solução Exata vs {name}', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()