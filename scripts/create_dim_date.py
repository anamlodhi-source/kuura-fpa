import pandas as pd
import holidays
from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
dim_market = pd.read_csv(data_folder / "dim_market.csv")

years = range(2024, 2028)
dates = pd.date_range("2024-01-01", "2027-12-31", freq="D")

rows = []
for code in dim_market["country_code"]:
    if code == "SE":
        country_holidays = holidays.Sweden(years=years, include_sundays=False)
    else:
        country_holidays = holidays.country_holidays(code, years=years)

    for day in dates:
        holiday_name = country_holidays.get(day.date())
        is_weekend = day.weekday() >= 5
        rows.append({
            "date": day.date(),
            "country_code": code,
            "weekday": day.day_name(),
            "is_weekend": is_weekend,
            "is_holiday": holiday_name is not None,
            "holiday_name": holiday_name,
            "is_business_day": not is_weekend and holiday_name is None,
        })

dim_date = pd.DataFrame(rows)

print(dim_date.head(10))
print("Total rows:", len(dim_date))
print("Holidays per country:")
print(dim_date[dim_date["is_holiday"]].groupby("country_code").size())

dim_date.to_csv(data_folder / "dim_date.csv", index=False)
print("Saved dim_date.csv")