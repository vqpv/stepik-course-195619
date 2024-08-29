def count_leap_years(year_1, year_2):
    c = 0
    for year in range(year_1, year_2):
        if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
            c += 1
    return c
