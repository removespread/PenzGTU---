number = float(input("Введите число: "))
n = int(input("Введите степень корня: "))

guess = 1
increment = 0.1

while guess ** n < number:
    guess = guess + increment

if abs(guess ** n - number) > abs((guess - increment) ** n - number):
    guess = guess - increment

print("Приближенное значение корня", n, "-ой степени из", number, "равно", round(guess, 3))

# float() - преобразование строки в число с плавающей точкой
# int() - преобразование строки в целое число
# ** - возведение в степень
# abs() - абсолютное значение числа
# round() - округление числа до заданного количества знаков после запятой