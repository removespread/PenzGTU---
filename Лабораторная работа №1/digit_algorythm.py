number = int(input("Введите целое число: "))
original_number = number

thousands = number // 1000
number = number % 1000

hundreds = number // 100
number = number % 100

tens = number // 10
ones = number % 10

print("Разложение числа", original_number, "на разряды:")
if thousands > 0:
    print(thousands * 1000)
if hundreds > 0:
    print(hundreds * 100)
if tens > 0:
    print(tens * 10)
if ones > 0:
    print(ones)

# int() - преобразование строки в целое число
# // - целочисленное деление
# % - остаток от деления