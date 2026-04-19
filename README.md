# 🛢️ Strait of Hormuz Oil Shock Simulator

> **How does a war in the Middle East hit your fuel bill in India?**  
> This project models the economic transmission of a Hormuz blockage — from global oil supply to India's Current Account Deficit.

---

## 📌 Why This Matters Right Now

On **February 28, 2026**, the United States and Israel launched strikes against Iran.  
Iran responded by **closing the Strait of Hormuz** — the single most important oil chokepoint on Earth.

- ~21 million barrels of oil pass through the Strait **every day**
- That is roughly **21% of global oil supply**
- India imports **4.8 million barrels/day** — 85% of its total consumption

A sustained blockage does not just raise petrol prices.  
It widens the trade deficit, weakens the rupee, and stokes domestic inflation.

**This project quantifies exactly how much.**

---

## 🔍 What This Project Does

Simulates **4 blockage scenarios** (10%, 25%, 50%, 100%) and calculates:

| Output | Description |
|--------|-------------|
| 🔺 Oil Price Spike | $/barrel increase using short-run elasticity model |
| 💸 Extra Import Bill | Additional annual cost to India in billion USD |
| 📉 CAD Impact | Widening of Current Account Deficit as % of GDP |
| 💱 Rupee Depreciation | Estimated INR/USD movement via pass-through coefficient |

---

## ⚙️ The Economics Behind It
ΔP/P = -(ΔS/S) / (ε_demand - ε_supply)

**Derived from first principles:**
Equilibrium condition:    ΔQd = ΔQs
Substituting elasticity:  ε_demand × ΔP/P = ε_supply × ΔP/P + ΔS/S
Rearranging:              ΔP/P × (ε_demand - ε_supply) = ΔS/S
Therefore:                ΔP/P = -(ΔS/S) ÷ (ε_demand - ε_supply)

Where:
- `ΔS/S` = percentage reduction in global oil supply from Hormuz closure
- `ε_demand` = **-0.10** (oil demand is highly inelastic in the short run)
- `ε_supply` = **+0.10** (supply is also inelastic — cannot pivot overnight)

The price impact then transmits to India through:
Extra Import Cost ($B) = India daily imports × ΔPrice × 365 / 1000
CAD Impact (% GDP)     = Extra Cost / India GDP × 100
Rupee Depreciation     = (ΔPrice / 10) × Pass-through coefficient

---

## 📊 Key Findings

| Scenario | Oil Price | Price Spike | Extra Import Bill | CAD Impact | New Rupee Rate |
|----------|-----------|-------------|-------------------|------------|----------------|
| 10% blockage | $88.24 | +$8.24/bbl | $14.44B/yr | +0.39% GDP | ₹84.33/$ |
| 25% blockage | $100.59 | +$20.59/bbl | $36.05B/yr | +0.97% GDP | ₹84.82/$ |
| 50% blockage | $121.18 | +$41.18/bbl | $72.10B/yr | +1.95% GDP | ₹85.65/$ |
| 100% blockage | $162.35 | +$82.35/bbl | $144.13B/yr | +3.90% GDP | ₹87.29/$ |

**Key insight:** A 100% Hormuz closure doubles oil prices — reaching 1973 Arab oil embargo levels.  
Even a 10% disruption costs India **$14.44 billion extra annually.**

---

## 📁 Project Structure
hormuz_shock_simulator/
│
├── data/
│   └── constants.py        # Base values — oil price, elasticities, India macro
│
├── model/
│   └── shock_model.py      # Core elasticity-based price shock formula
│
├── analysis/
│   └── india_impact.py     # CAD, import bill, rupee transmission
│
└── main.py                 # Runs full simulation end-to-end

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.x` | Core language |
| `NumPy` | Numerical simulation and scenario arrays |
| `Pandas` | Data structuring and results table |

---

## 📂 Data Sources

| Data Point | Source |
|-----------|--------|
| Global oil supply | [IEA Oil Market Report 2024](https://www.iea.org/reports/oil-market-report-december-2024) |
| Hormuz throughput | [EIA Chokepoint Analysis](https://www.eia.gov/todayinenergy/detail.php?id=61002) |
| India crude imports | [PPAC Import Data](https://ppac.gov.in/import-export) |
| India GDP | [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN) |
| CAD impact estimates | [SBI Research](https://www.businesstoday.in/latest/economy/story/west-asia-conflict-may-hit-india-hard-oil-spike-could-raise-inflation-slow-gdp-sbi-research-519555-2026-03-07) |
| Rupee pass-through | [RBI Working Papers](https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=20738) |
| Short-run elasticities | [Hamilton (2009) — NBER](https://www.nber.org/papers/w14492) |

---

## ▶️ How to Run

```bash
git clone https://github.com/nemesis-ctrl/hormuz-shock-simulator
cd hormuz-shock-simulator
pip install numpy pandas
python main.py
```

---

## 🏛️ Policy Recommendations

Based on simulation findings, six policy interventions for India:

1. **Expand Strategic Petroleum Reserve** — from 66 to 90+ days of import cover
2. **Diversify import sources** — reduce Gulf concentration below 44%
3. **Pre-position RBI forex buffer** — $20-30B dedicated oil shock reserve
4. **Accelerate EV transition** — cut crude imports by ~0.8mb/d by 2030
5. **Strengthen IEA coordination** — faster access to emergency reserve releases
6. **Invest in pipeline alternatives** — reduce maritime Hormuz dependency

---

## 👤 Author

**Rishabh**  
Economics Honours, Ramjas College — University of Delhi  
Interests: Applied Macroeconomics · Energy Economics · Data Analysis


---

## 📜 Disclaimer

This is an academic simulation project built for learning purposes.  
All elasticity values and macro parameters are approximations from published literature.  
This is not financial or investment advice.


The core model uses the **price elasticity approach** to supply shocks:
