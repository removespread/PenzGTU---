weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))

bmi = weight / (height ** 2)

print("Ваш индекс массы тела (BMI):", bmi)

if bmi < 18.5:
    comment = "Недовес"
elif bmi < 25:
    comment = "Норма"
elif bmi < 30:
    comment = "Избыточный вес"
else:
    comment = "Ожирение"

print("Комментарий:", comment)

# float() - преобразование строки в число с плавающей точкой
# ** - возведение в степень
# if, elif, else - условные операторы для определения категории BMI