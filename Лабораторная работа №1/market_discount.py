quantity = int(input("Введите количество предметов: "))
price = float(input("Введите стоимость одного предмета: "))

total_cost = quantity * price

if quantity > 20:
    discount = 0.2  # 20% скидка
elif quantity > 10:
    discount = 0.1  # 10% скидка
else:
    discount = 0

discount_amount = total_cost * discount
final_cost = total_cost - discount_amount

print("Общая стоимость:", total_cost)
if discount > 0:
    print("Сумма скидки:", discount_amount)
    print("Стоимость со скидкой:", final_cost)
else:
    print("Скидка не применяется")

# int() - преобразование строки в целое число
# float() - преобразование строки в число с плавающей точкой
# if, elif, else - условные операторы для определения скидки