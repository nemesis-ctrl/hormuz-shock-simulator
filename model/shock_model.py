# Core price shock calculator using short-run elasticity model

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.constants import (
    GLOBAL_SUPPLY_MBD,
    HORMUZ_THROUGHPUT_MBD,
    HORMUZ_SHARE,
    BASE_OIL_PRICE,
    ELASTICITY_DEMAND,
    ELASTICITY_SUPPLY
)

import numpy as np

# Step 1: Define your 4 scenarios 
BLOCKAGE_SCENARIOS = np.array([0.10, 0.25, 0.50, 1.00])
SCENARIO_LABELS = ["10%", "25%", "50%", "100%"]

#  Step 2: Calculate supply reduction for each scenario
def calc_supply_reduction(blockage_pct):
    """
    How much of global supply is lost?
    If 25% of Hormuz is blocked:
    Supply lost = 0.25 × 0.206 = 5.15% of global supply
    """
    return blockage_pct * HORMUZ_SHARE

#  Step 3: Apply the elasticity formula
def calc_price_shock(supply_reduction_pct):
    """
    ΔP/P = -(ΔS/S) / (ε_demand - ε_supply)
    Returns the % change in oil price
    """
    denominator = ELASTICITY_DEMAND - ELASTICITY_SUPPLY
    price_change_pct = -(supply_reduction_pct) / denominator
    return price_change_pct

#  Step 4: Calculate new absolute price 
def calc_new_price(price_change_pct):
    """
    New price = Base price × (1 + ΔP/P)
    """
    return BASE_OIL_PRICE * (1 + price_change_pct)

#  Step 5: Run all scenarios together
def run_all_scenarios():
    """
    Returns a dictionary with results for all 4 scenarios
    """
    results = {}

    for i, blockage in enumerate(BLOCKAGE_SCENARIOS):
        label = SCENARIO_LABELS[i]

        supply_reduction = calc_supply_reduction(blockage)
        price_change_pct = calc_price_shock(supply_reduction)
        new_price = calc_new_price(price_change_pct)
        price_spike = new_price - BASE_OIL_PRICE

        results[label] = {
            "blockage_pct"       : blockage,
            "supply_reduction_pct": round(supply_reduction * 100, 2),
            "price_change_pct"   : round(price_change_pct * 100, 2),
            "new_price_usd"      : round(new_price, 2),
            "price_spike_usd"    : round(price_spike, 2),
        }

    return results
