year = int(input("введите год"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, "да это високосный год")
else:
    print("нет это невисокосный год")