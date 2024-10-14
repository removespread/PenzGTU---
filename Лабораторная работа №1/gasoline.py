consumption = float(input("Введите расход топлива на 100 км: "))
distance = float(input("Введите расстояние в км: "))

fuel_needed = (consumption * distance) / 100

print("Необходимо топлива:", fuel_needed, "литров")

# float(input()) - получение числа с плавающей точкой от пользователя

# (consumption * distance) / 100 - формула для расчета необходимого количества топлива

# print - вывод результата, аргументы разделены запятыми