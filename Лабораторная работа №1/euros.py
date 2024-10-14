rubles = float(input("Введите количество рублей: "))
exchange_rate = float(input("Введите курс евро (стоимость 1 евро в рублях): "))

euros = rubles / exchange_rate

print(rubles, "рублей =", euros, "евро")

# float(input()) - получение числа с плавающей точкой от пользователя

# rubles / exchange_rate - формула для конвертации рублей в евро

# print - вывод результата, аргументы разделены запятыми