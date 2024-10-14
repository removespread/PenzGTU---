import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Корни: x1 =", x1, ", x2 =", x2)
elif discriminant == 0:
    x = -b / (2*a)
    print("Корень: x =", x)
else:
    print("Нет действительных корней")

# math.sqrt() - функция для вычисления квадратного корня

# b**2 - возведение b в квадрат

# Условия для определения количества корней:
# discriminant > 0 - два корня
# discriminant == 0 - один корень
# discriminant < 0 - нет действительных корней
# подключение библиотеки - import math