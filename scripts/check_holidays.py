import holidays

fi_holidays = holidays.Sweden(years=2026)

for date, name in sorted(fi_holidays.items()):

    print(date, name)