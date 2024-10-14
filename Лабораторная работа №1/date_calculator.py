from datetime import datetime

date1 = input("Введите первую дату (DD-MM-YYYY): ")
date2 = input("Введите вторую дату (DD-MM-YYYY): ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs((date2 - date1).days)

print("Количество дней между датами:", difference)

# datetime.strptime() - преобразует строку в объект даты
# "%d-%m-%Y" - формат даты: день-месяц-год

# abs() - получение абсолютного значения разницы
# .days - получение количества дней из разницы дат

# сделано полностью через пакет datetime, все неймспейсы взяты с документации