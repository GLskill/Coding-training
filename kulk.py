from colorama import init
from colorama import Fore, Back, Style

init()

#print(Fore.BLACK)
#print(Back.GREEN)

what = input("что делаем ? (+, -): ")

print(Back.CYAN)

a = float(input("Введи первое число : "))
b = float(input("Введи второе число : "))

print(Back.YELLOW)

if what == "+":
    c = a + b
    print(f"Результат : {c}")
elif what == "-":
    c = a - b
    print(f"Результат : {c}")
else:
    print("Не верно заебал , выбери другую операцию")


