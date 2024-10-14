initial_cost = float(input("Введите начальную стоимость товара: "))
lifespan = int(input("Введите срок службы товара (в годах): "))
depreciation_rate = float(input("Введите процент амортизации: "))

current_cost = initial_cost
year = 1

while year <= lifespan:
    depreciation = current_cost * (depreciation_rate / 100)
    current_cost = current_cost - depreciation
    print("Год", year, ": Стоимость =", round(current_cost, 2), "$")
    year = year + 1

# float() - преобразование строки в число с плавающей точкой
# int() - преобразование строки в целое число
# while - цикл для расчета амортизации по годам
# round() - округление числа до заданного количества знаков после запятой