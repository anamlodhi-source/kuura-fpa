import pandas as pd
from pathlib import Path

markets = [
    {"market": "Finland",     "country_code": "FI", "tier": "Core",   "currency": "EUR", "launch_year": 2019},
    {"market": "Sweden",      "country_code": "SE", "tier": "Core",   "currency": "SEK", "launch_year": 2020},
    {"market": "Norway",      "country_code": "NO", "tier": "Growth", "currency": "NOK", "launch_year": 2022},
    {"market": "Denmark",     "country_code": "DK", "tier": "Growth", "currency": "DKK", "launch_year": 2022},
    {"market": "Germany",     "country_code": "DE", "tier": "Growth", "currency": "EUR", "launch_year": 2023},
    {"market": "Estonia",     "country_code": "EE", "tier": "Early",  "currency": "EUR", "launch_year": 2024},
    {"market": "Netherlands", "country_code": "NL", "tier": "Early",  "currency": "EUR", "launch_year": 2025},
    {"market": "Poland",      "country_code": "PL", "tier": "Early",  "currency": "PLN", "launch_year": 2025},
]

dim_market = pd.DataFrame(markets)
print(dim_market)

output_file = Path(__file__).parent.parent / "data" / "dim_market.csv"
dim_market.to_csv(output_file, index=False)
print("Saved to", output_file)