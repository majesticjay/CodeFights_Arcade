def centuryFromYear(year):
    cen = year // 100
    r = year % 100
    if r == 0:
        return cen
    else:
        return cen + 1
