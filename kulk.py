from colorama import init
from colorama import Fore, Back, Style

init()

#print(Fore.BLACK)
#print(Back.GREEN)

what = input("Writh ? (+, -): ")

print(Back.CYAN)

a = float(input("First number : "))
b = float(input("Second Number: "))

print(Back.YELLOW)

if what == "+":
    c = a + b
    print(f"Result : {c}")
elif what == "-":
    c = a - b
    print(f"Result : {c}")
else:
    print("incorrect error in the symbol")


