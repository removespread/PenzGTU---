month = input("Введите название месяца: ").lower()

if month == "декабрь" or month == "январь" or month == "февраль":
    season = "Зима"
elif month == "март" or month == "апрель" or month == "май":
    season = "Весна"
elif month == "июнь" or month == "июль" or month == "август":
    season = "Лето"
elif month == "сентябрь" or month == "октябрь" or month == "ноябрь":
    season = "Осень"
else:
    season = "Неизвестный месяц"

print("Время года:", season)

# .lower() - приведение строки к нижнему регистру
# or - логический оператор "или"