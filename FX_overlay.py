# FX overlay
import numpy as np
import pandas as pd

# initial values
notional_eur = 10_000_000  # EUR
initial_fx = 1.10          # initial fx rate EURUSD (1 EUR = 1.10 USD)
hedge_ratio = 0.75         # % of ptf hedged with FX forward

# hedged position in USD (hedged with FX forward)
hedged_usd = notional_eur * initial_fx * hedge_ratio

# for each scenario, calculate:
# - ptf value in USD (non hedged)
# - ptf value in USD hedged with FX forward fixed at 1.10
# - profit/loss from currency overlay (hedged vs unhedged)


def simulate_currency_overlay(notional_eur, initial_fx, hedge_ratio, scenarios):
    
    hedged_usd = notional_eur * initial_fx * hedge_ratio
    
    results = []

    for scenario, final_fx in scenarios.items():
        unhedged_usd = notional_eur * (1 - hedge_ratio) * final_fx
        total_usd = unhedged_usd + hedged_usd
        total_unhedged = notional_eur * final_fx
        profit_overlay = total_usd - total_unhedged

        results.append({
            "Scenario": scenario,
            "Final FX": final_fx,
            "Unhedged USD": unhedged_usd,
            "Hedged USD": hedged_usd,
            "Total USD (with overlay)": total_usd,
            "Total USD (no overlay)": total_unhedged,
            "Profit from overlay": profit_overlay
        })

    return pd.DataFrame(results).round(2)

# 3 different scenarios at 6 months
# - EUR/USD appreciates to 1.15
# - EUR/USD stable at 1.10
# - EUR/USD depreciates to 1.05

scenarios = {
    "EUR/USD appreciates to 1.15": 1.15,
    "EUR/USD stable at 1.10": 1.10,
    "EUR/USD depreciates to 1.05": 1.05,
}

# simulate the overlay

df_overlay = simulate_currency_overlay(
    notional_eur=10_000_000,
    initial_fx=1.10,
    hedge_ratio=0.75,
    scenarios=scenarios
)

print(df_overlay)

df_overlay.to_excel("currency_overlay_scenarios.xlsx", index=False)
