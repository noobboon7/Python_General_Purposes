import datetime, time


def calc_age(year, day, month):
    dob = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - year
    if dob.month >= today.month:
        if dob.day > today.day:
            age -= 1
    return age


print(calc_age(2004, 10, 1))
