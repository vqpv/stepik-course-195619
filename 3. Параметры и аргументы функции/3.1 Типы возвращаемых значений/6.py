def get_leap_years(yaer_1, yaer_2):
    return [year for year in range(yaer_1, yaer_2) if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0]
