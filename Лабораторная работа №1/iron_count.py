initial_thickness = float(input("Введите начальную толщину металла: "))
desired_thickness = float(input("Введите желаемую толщину металла: "))

rolls = 0
current_thickness = initial_thickness

while current_thickness > desired_thickness:
    current_thickness = current_thickness / 2
    rolls = rolls + 1

print("Количество прокатов:", rolls)

# float() - преобразование строки в число с плавающей точкой
# while - цикл для повторения операции прокатки