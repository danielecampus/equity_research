# playing with Convertible Bonds
import os
print("Current working directory:", os.getcwd())

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.stats import norm

# Parametri di input per il pricing della convertible bond (Black-Scholes base)
S = 60            # prezzo corrente dell'azione
K = 50            # conversion price (strike dell'opzione)
T = 3             # tempo alla scadenza (anni)
r = 0.02          # tasso risk-free
sigma = 0.30      # volatilità
conversion_ratio = 20  # numero di azioni per ogni bond convertito

# Calcolo d1 e d2 per Black-Scholes
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

# Valore della call (embedded option)
call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
embedded_option_value = conversion_ratio * call_price

# Calcolo del bond floor (valore attuale dei flussi obbligazionari)
face_value = 1000
coupon_rate = 0.02
coupon = face_value * coupon_rate
discount_rate = 0.05  # tasso obbligazionario

# Valore attuale delle cedole e del rimborso
bond_floor = sum([coupon / (1 + discount_rate)**t for t in range(1, 4)]) + face_value / (1 + discount_rate)**3

# Fair value del convertible
convertible_fair_value = bond_floor + embedded_option_value

# Simulazione Dynamic Alpha: performance attesa del portafoglio rispetto a benchmark
# Supponiamo che il portafoglio sia composto per il 50% da convertibles e per il 50% da azioni
np.random.seed(42)  # Set a fixed seed for reproducibility

returns_convertible = np.random.normal(0.06, 0.08, 1000)
returns_benchmark = np.random.normal(0.05, 0.07, 1000)

returns_portfolio = 0.5 * returns_convertible + 0.5 * returns_benchmark  # Refine portfolio return model

# Calcolo alpha dinamico = rendimento in eccesso rispetto al benchmark
dynamic_alpha = np.mean(returns_portfolio) - np.mean(returns_benchmark)

# Output principali
print(embedded_option_value)
print(bond_floor)
print(convertible_fair_value)
print(dynamic_alpha)

# Visualizzazione della simulazione
plt.figure(figsize=(12, 6))
plt.hist(returns_portfolio, bins=30, alpha=0.5, label='Portfolio Returns')
plt.hist(returns_benchmark, bins=30, alpha=0.5, label='Benchmark Returns')
plt.axvline(np.mean(returns_portfolio), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(np.mean(returns_benchmark), color='orange', linestyle='dashed', linewidth=1)
plt.title('Simulated Returns Distribution')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Salva il grafico
plt.savefig(r"c:\Users\danie\OneDrive\GitHub\equity_research\dynamic_alpha_chart.png")
plt.show()

### Animation

fig, ax = plt.subplots(figsize=(12, 6))

def update(frame):
    ax.clear()

    current_returns_portfolio = returns_portfolio[:frame]
    current_returns_benchmark = returns_benchmark[:frame]
    
    ax.hist(current_returns_portfolio, bins=30, alpha=0.5, label='Portfolio Returns')
    ax.hist(current_returns_benchmark, bins=30, alpha=0.5, label='Benchmark Returns')
    ax.axvline(np.mean(current_returns_portfolio), color='blue', linestyle='dashed', linewidth=1)
    ax.axvline(np.mean(current_returns_benchmark), color='orange', linestyle='dashed', linewidth=1)
    ax.set_title('Simulated Returns Distribution (Frame {})'.format(frame))
    ax.set_xlabel('Returns')
    ax.set_ylabel('Frequency')
    ax.legend()
    ax.grid(True)

num_frames = len(returns_portfolio)

ani = FuncAnimation(fig, update, frames=range(10, num_frames, 10), repeat=False)

ani.save(r"c:\Users\danie\OneDrive\GitHub\equity_research\dynamic_alpha_animation.gif", writer=PillowWriter(fps=10))
plt.show()

try:
    ani.save(r"c:\Users\danie\OneDrive\GitHub\equity_research\dynamic_alpha_animation.gif", writer='imagemagick')
    print("GIF saved successfully!")
except Exception as e:
    print("Error saving GIF:", e)

