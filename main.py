from model.shock_model import run_all_scenarios
results = run_all_scenarios()
print("  STRAIT OF HORMUZ — OIL PRICE SHOCK SIMULATION")
for scenario, data in results.items():
    print(f"\nScenario: {scenario} blockage")
    print(f"  Supply lost globally : {data['supply_reduction_pct']}%")
    print(f"  Price change         : +{data['price_change_pct']}%")
    print(f"  New oil price        : ${data['new_price_usd']}/barrel")
    print(f"  Price spike          : +${data['price_spike_usd']}/barrel")


from analysis.india_impact import run_india_impact

results = run_india_impact()

print("   STRAIT OF HORMUZ — FULL INDIA MACRO IMPACT SIMULATION")

for scenario, data in results.items():
    print(f"\nScenario: {scenario} blockage")
    print(f"  Oil price spike      : +${data['price_spike_usd']}/barrel")
    print(f"  Extra import bill    : ${data['extra_import_bill_b']}B/year")
    print(f"  CAD impact           : +{data['cad_pct_gdp']}% of GDP")
    print(f"  Rupee depreciation   : −₹{data['rupee_depreciation']}")
    print(f"  New rupee rate       : ₹{data['new_rupee_rate']}/$")



