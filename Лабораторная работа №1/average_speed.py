v1 = float(input("Введите скорость на первой половине пути (км/ч): "))
v2 = float(input("Введите скорость на второй половине пути (км/ч): "))

average_speed = 2 / ((1/v1) + (1/v2))

print("Средняя скорость:", round(average_speed, 2), "км/ч")

# 2 / ((1/v1) + (1/v2)) - формула для расчета средней скорости
# Используется гармоническое среднее, так как расстояния равны

# round(average_speed, 2) - округление до двух знаков после запятой