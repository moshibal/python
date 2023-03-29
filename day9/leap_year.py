def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "leap year"
            else:
                return "not leap year"
        else:
            return "leap year"
    else:
        return "not leap year"


def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31]
    is_leap_year = is_leap(year)
    if (is_leap_year == "leap year"):
        month_days[1] = 29
        return month_days[month-1]
    else:
        return month_days[month-1]


year = int(input("enter a year: "))
month = int(input("enter a month: "))
days = days_in_months(year, month)
print(days)
