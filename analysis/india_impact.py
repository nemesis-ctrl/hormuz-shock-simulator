# Translates oil price shock into India macro consequences
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.constants import (
    INDIA_IMPORTS_MBD,
    INDIA_GDP_USD_B,
    INDIA_RUPEE_PASSTHROUGH,
    INDIA_RUPEE_BASE
)

from model.shock_model import run_all_scenarios

# Extra annual import bill 
def calc_import_bill(price_spike_usd):
    """
    Extra cost = price spike × daily imports × 365 days
    Result in billion USD
    """
    extra_cost_per_day = price_spike_usd * INDIA_IMPORTS_MBD
    extra_cost_annual  = extra_cost_per_day * 365
    return round(extra_cost_annual / 1000, 2)  # convert to billions

#  CAD impact as % of Gdp
def calc_cad_impact(extra_import_bill_b):
    """CAD widens by the extra import cost
    Expressed as % of GDP"""
    cad_pct_gdp = (extra_import_bill_b / INDIA_GDP_USD_B) * 100
    return round(cad_pct_gdp, 2)

#  Rupee depreciation 
def calc_rupee_impact(price_spike_usd):
    
    """Every $10 rise → rupee depreciates by passthrough coefficient"""
    depreciation = (price_spike_usd / 10) * INDIA_RUPEE_PASSTHROUGH
    new_rupee    = INDIA_RUPEE_BASE + depreciation
    return round(depreciation, 2), round(new_rupee, 2)

# Run full India impact for all scenarios 
def run_india_impact():
    price_results = run_all_scenarios()
    india_results = {}

    for scenario, data in price_results.items():
        price_spike = data["price_spike_usd"]

        import_bill          = calc_import_bill(price_spike)
        cad_impact           = calc_cad_impact(import_bill)
        rupee_drop, new_rate = calc_rupee_impact(price_spike)

        india_results[scenario] = {
            "price_spike_usd"    : price_spike,
            "extra_import_bill_b": import_bill,
            "cad_pct_gdp"        : cad_impact,
            "rupee_depreciation" : rupee_drop,
            "new_rupee_rate"     : new_rate,
        }

    return india_results