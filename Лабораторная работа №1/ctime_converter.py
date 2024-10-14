total_seconds = int(input("Введите количество секунд: "))

days = total_seconds // (24 * 3600)
remaining_seconds = total_seconds % (24 * 3600)

hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(days, "дней,", hours, "часов,", minutes, "минут,", seconds, "секунд")

# // - целочисленное деление
# % - остаток от деления

# 24 * 3600 - количество секунд в сутках
# 3600 - количество секунд в часе
# 60 - количество секунд в минуте