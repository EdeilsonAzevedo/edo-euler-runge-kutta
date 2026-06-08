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

def plot_compare2(t_1, y_1, t_2, y_2, first_name="", second_name=""):
    plt.figure(figsize=(10, 6))

    plt.plot(t_1, y_1, label=first_name, color='blue', linewidth=2)

    plt.plot(t_2, y_2, label=second_name, 
             color='red', linestyle='--', marker='o', linewidth=1, markersize=5)

    plt.title(f'{first_name} vs {second_name}', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()

def plot_compare3(t_1, y_1, t_2, y_2, t_3, y_3, first_name="", second_name="", third_name=""):
    plt.figure(figsize=(10, 6))

    plt.plot(t_1, y_1, label=first_name, color='blue', linewidth=2)
    plt.plot(t_2, y_2, label=second_name, color='green', linestyle='--', marker='o', linewidth=1, markersize=5)
    plt.plot(t_3, y_3, label=third_name, color='red', linestyle='--', marker='o', linewidth=1, markersize=5)

    plt.title(f'{first_name} vs {second_name} vs {third_name}', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()

def plot_compare4(t_1, y_1, t_2, y_2, t_3, y_3, t_4, y_4, first_name="", second_name="", third_name="", fourth_name=""):
    plt.figure(figsize=(10, 6))

    plt.plot(t_1, y_1, label=first_name, color='blue', linewidth=2)
    plt.plot(t_2, y_2, label=second_name, color='green', linestyle='--', marker='o', linewidth=1, markersize=5)
    plt.plot(t_3, y_3, label=third_name, color='red', linestyle='--', marker='o', linewidth=1, markersize=5)
    plt.plot(t_4, y_4, label=fourth_name, color='orange', linestyle='--', marker='o', linewidth=1, markersize=5)

    plt.title(f'{first_name} vs {second_name} vs {third_name} vs {fourth_name}', fontsize=14)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()