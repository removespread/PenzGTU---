percent_increase = float(input("Введите процент увеличения инвестиций в год: "))

years = 0
investment = 100  # Начальная сумма инвестиций

while investment < 200:  # Пока инвестиции не удвоились
    investment = investment + (investment * percent_increase / 100)
    years = years + 1

print("Через", years, "лет")

# float() - преобразование строки в число с плавающей точкой
# while - цикл для повторения расчета по годам