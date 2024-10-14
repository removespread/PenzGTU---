number = int(input("Введите число: "))

divisible_by_2 = number % 2 == 0
divisible_by_5 = number % 5 == 0
divisible_by_10 = number % 10 == 0

print("Делится на 2:", divisible_by_2)
print("Делится на 5:", divisible_by_5)
print("Делится на 10:", divisible_by_10)

# int(input()) - получение целого числа от пользователя

# % - операция получения остатка от деления
# == - оператор сравнения, возвращает True, если значения равны

# print - вывод результата, каждая проверка на отдельной строке