# Métodos de Euler e Runge-Kutta para EDOs

> Implementação e análise comparativa dos métodos numéricos de Euler (explícito e implícito) e Runge-Kutta (RK2, RK4) para resolução de Equações Diferenciais Ordinárias (EDOs).

---

## 📁 Estrutura do Repositório

```
edo-euler-runge-kutta/
│
├── src/                        # Implementações dos métodos
│   ├── __init__.py
│   ├── euler.py                # Euler explícito e implícito
│   ├── runge_kutta.py          # RK2 (Heun) e RK4
│   └── utils.py                # Funções auxiliares (erro, plotagem)
│
├── notebooks/                        # Aplicações a problemas clássicos
│   ├── lotka_volterra.ipynb            # Dinâmica predador-presa (biologia)
│   ├── sir_model.ipynb                 # Epidemias — modelo Kermack-McKendrick
│   ├── van_der_pol.ipynb               # Oscilador não-linear / circuitos (stiff)
│   ├── lorenz_system.ipynb             # Caos determinístico / atrator de Lorenz
│   └── nonlinear_pendulum.ipynb        # Pêndulo não-linear + integrais elípticas
│
├── tests/                      # Testes unitários
│   └── test_methods.py
│
├── docs/
│   └── references.md           # Referências bibliográficas
│   └── apresentação.md
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧮 Métodos Implementados

| Método | Ordem | Arquivo |
|--------|-------|---------|
| Euler Explícito | 1ª | `src/euler.py` |
| Euler Implícito (Backward) | 1ª | `src/euler.py` |
| Runge-Kutta 2ª ordem (Heun) | 2ª | `src/runge_kutta.py` |
| Runge-Kutta 4ª ordem (clássico) | 4ª | `src/runge_kutta.py` |

---

## 🔬 Exemplos — Problemas Clássicos

| Arquivo | Problema | Área | Destaque |
|---------|----------|------|----------|
| `lotka_volterra.py` | Dinâmica predador-presa | Biologia / Ecologia | Órbitas periódicas no plano de fase |
| `van_der_pol.py` | Oscilador de Van der Pol | Física / Engenharia | Limite-ciclo; problema *stiff* |
| `lorenz_system.py` | Atrator de Lorenz | Caos / Meteorologia | Sensibilidade às condições iniciais |
| `nonlinear_pendulum.py` | Pêndulo não-linear | Mecânica clássica | Comparação com solução analítica exata |
| `sir_model.py` *(possível)* | Modelo SIR — Kermack-McKendrick | Epidemiologia | R₀, pico de infectados, efeito de intervenções |
| `seir_model.py` *(possível)* | Modelo SEIR — com período de incubação | Epidemiologia | 4 EDOs acopladas; mais realista que o SIR |

---

## ⚙️ Como usar

```bash
# Clone o repositório
git clone https://github.com/EdeilsonAzevedo/edo-euler-runge-kutta.git
cd edo-euler-runge-kutta

# Instale as dependências
pip install -r requirements.txt

# Execute um exemplo
python examples/exponential_decay.py

# Ou abra os notebooks
jupyter notebook notebooks/
```

---

## 📦 Dependências

```
numpy
matplotlib
scipy
jupyter
```

---

## 📚 Referências

Veja [`docs/references.md`](docs/references.md) para a lista completa de livros e artigos utilizados.

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Edeilson Azevdo | edeilsonazevedo |
| ... | @... |

---

## 📄 Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.