time_24 = input("Введите время в 24-часовом формате (ЧЧ:ММ): ")

hours, minutes = time_24.split(':')
hours = int(hours)
minutes = int(minutes)

if hours == 0:
    hours_12 = 12
    period = "AM"
elif hours < 12:
    hours_12 = hours
    period = "AM"
elif hours == 12:
    hours_12 = 12
    period = "PM"
else:
    hours_12 = hours - 12
    period = "PM"

if minutes < 10:
    minutes_str = "0" + str(minutes)
else:
    minutes_str = str(minutes)

time_12 = str(hours_12) + ":" + minutes_str + " " + period

print("Время в 12-часовом формате:", time_12)

# split(':') - разделяет строку по ':'
# int() - преобразует строку в целое число
# str() - преобразует число обратно в строку