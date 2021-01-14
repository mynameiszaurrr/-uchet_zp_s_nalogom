month = int(input("Введите месяц "))
if month <= 0 or month >= 13:
    while month <= 0 or month >= 13:
        month = int(input("Неверный месяц! ВВедите число еще раз!\n"))
day = int(input("Введите дату "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day <= 0 or day >= 32:
        while day <= 0 or day >= 32:
            day = int(input("Неверный день! ВВедите число еще раз!\n"))
elif month == 2:
    if day <= 0 or day >= 30:
        while day <= 0 or day >= 30:
            day = int(input("Неверный день! ВВедите число еще раз!\n"))
else:
    if day <= 0 or day >= 31:
        while day <= 0 or day >= 31:
            day = int(input("Неверный день! ВВедите число еще раз!\n"))
year = int(input("Введите год "))
if year <= 0 or year >= 10000:
    while year <= 0 or year >= 10000:
        year = int(input("Неверный год! ВВедите число еще раз!\n"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    day = day
else:
    if day == 29:
        day = int(input("Внимание! Год не високосный! Допустимое число дней в невискосном году - менее 29. Введите "
                        "новое число дня! "))
        while day >= 29 or day <= 0:
            day = int(input("Внимание! Год не високосный! Допустимое число дней в невискосном году - менее 29. "
                            "Введите новое число дня! "))
if day <= 9:
    day = str(day).rjust(2, '0')
if month <= 9:
    month = str(month).rjust(2, '0')
if year <= 999:
    year = str(year).rjust(4, '0')
print(f'{day}/{month}/{year} (День/Месяц/Год)')