# print("Hello","world!")
# print("Hello,world!")
# print("Hello", "World !", sep=",")
# print("First row")
# print("second row")
# print("First row",end=" ")
# print("second row")
# input("Pleas enter somthing")
# name = input("enter you name")
# print(name)
#
# print("----------------------------------------------------------------")
#
# name1 = "alice"
# age = 25
# print(name1, age)
#
# name2, age2 = "Bitcoin", 47000
# print(name2, age2)
#
# print("----------------------------------------------------------------")
#
# variable = 1
# print(type(variable))
#
# variable2 = "hello AMG"
# print(type(variable2))
#
# print("----------------------------------------------------------------")
#
# my_integer = 10
# my_float = 25.544342
#
# my_float = int(my_float)
# print(my_float)
#
# my_float = round(my_float)
# print(my_float)
#
# print("----------------------------------------------------------------")
#
# flat_number = 104
#
# entrance_number = (flat_number - 1) // 20 + 1
# floor_number = (flat_number - 1) % 20 // 4 + 1
#
# print(entrance_number)
# print(floor_number)
#
# print("----------------------------------------------------------------")
#
# is_student = True
# is_graduated = False
#
# print(is_graduated)
# x = 10
# y = 10
# print(x == y)
#
# x = 9
# y = 10
# print(x == y)
#
# x = 10
# y = 10
# not_equal = x != y
# print(not_equal)
#
# print("----------------------------------------------------------------")
#
# if False:
#     print("Hello, World")
#
# x = 0
# if x > 0:
#     print ("x is positive")
# elif x <0:
#     print("x is negative")
# else:
#     print("x is zero")
#
# x = 10
# y = 20
# if x > 0 and y > 0:
#     print("x and y are positive")
#
# print("----------------------------------------------------------------")
#
# message = ""
# if bool(message):
#     print("message is not empty")
#
# print("----------------------------------------------------------------")
#
# year = 2000
#
# if year % 4 == 0 and year % 100 != 0:
#     print("year is leap")
# elif year % 400 ==0:
#     print("year is leap")
# else:
#     print("year is not leap")
#
# print("----------------------------------------------------------------")
#
# my_string = """
# Python is a versatile programming language known for its simplicity and readability.
# With a rich ecosystem of libraries and frameworks, it facilitates rapid development and is widely used for web development, data analysis, artificial intelligence, and more.
# Whether you're a beginner or an experienced developer, Python's syntax and community support make it an excellent choice for a variety of applications.
# """
# print(my_string)
#
# first_name = "Aegis"
# last_name = "Gskill 3000 Hz"
# full_name = first_name + " " + last_name
#
# print(full_name)
#
# length = len(full_name)
#
# print(length)
#
# print("----------------------------------------------------------------")
#
# my_integer = 100
# my_string = str(my_integer)
#
# my_int = int ("10")
# print(type(my_integer + my_int))
#
# print("----------------------------------------------------------------")
#
# big_integer = 2 ** 10023
# print(len(str(big_integer)))
#
# my_string = "hello world"
# print("hello" in my_string)
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace("world","Python"))
# print(my_string.count("l"))
# print(my_string.isdigit())
#
# print("----------------------------------------------------------------")
#
# name = "Aegis"
# age = 3000
# print(f"hello, my name is {name} and i'm {age} years old")
#
# print("----------------------------------------------------------------")
#
# my_string = input("Enther a Number")
#
# if my_string.isdigit():
#     my_integer= int(my_string)
#     print(my_integer)
# else:
#     print(f"{my_string} is not a numb")
#
# print("----------------------------------------------------------------")
#
# word = "AMGobvesMersedes"
# my_list = list(word)
# print(my_list)
#
# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = [6, 7, 8, 9]
# my_list3 = my_list1 + my_list2
#
# print(my_list3)
#
# print("----------------------------------------------------------------")
#
# fruits = ["apple", "banana", "chery"]
# fruits.append("watermelon")
#
# print(fruits)
#
# print("----------------------------------------------------------------")
#
# разварот списка 3 способа
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
#
# new_numbers = numbers[::-1]
# print(new_numbers)
#
# numbers.reverse()
# print(numbers)
#
# new_numbers = reversed(numbers)
# print(new_numbers)
#
# new_numbers = type(reversed(numbers))
# print(new_numbers)
#
# print("----------------------------------------------------------------")
#
# Зацикливание
#
# file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
#
# for file_name in file_names:
#     print(file_name)
#
# greeting = "hello, worldoo!"
# count_o = 0
# for loop in greeting:
#     if loop == "o":
#         count_o += 1
#         print(loop)
# print(count_o)
#
# students = ["Artur", "Billy", "Bob", "Davian", "Gray"]
#
# for student in students:
#     print(student)
#     for char in student:
#         print(char)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     print(num)
#
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#
# for num1 in numbers1:
#     if num1 == 10:
#         break
#     print(num1)
#
# range_object = range(15)
# print(range_object)
#
# numbers = list(range_object)
# print(numbers)
#
# numbers = [10, 11, 12, 14, 15, 16]
#
# for number in numbers:
#     number += 1
#
# print(numbers)
#
# numbers1 = [10, 11, 12, 14, 15, 16]
#
# for i in range(len(numbers1)):
#     numbers1[i] += 1
#
# print(numbers1)
#
# greeting = "Heloooo Woooorld"
#
# indexes = []
# count = 0
#
# for i in range(len(greeting)):
#     if greeting[i] == "o":
#         count += 1
#         indexes.append(i)
#
# print(count)
# print(indexes)
#
# print("----------------------------------------------------------------")
# ДЗ  сделать таблицу умнажения
#
# rows = 6
# columns = 6
#
# multiP_table = ""
#
# for i in range(1, rows + 1):
#     for j in range(1, columns + 1):
#         multiP_table += f"{i * j:3}"
#     multiP_table += "\n"
#
# print(multiP_table)
#
#
# def table_of_multiplication(n):
#     numbers = list(range(1, n + 1))
#
#     result = ""
#     for i in numbers:
#         for j in numbers:
#             result += f"{i} * {j} = {i * j}\t"
#         result += "\n"
#
#     return result
#
# print(table_of_multiplication(9))
#
# print("----------------------------------------------------------------")
#
# numbers = [10, 11, 12, 14, 15, 16]
# numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# average_1 = sum(numbers) / len(numbers)
# print(average_1)
#
# numbers = [10, 11, 12, 14, 15, 16]
# numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def find_average(numbers):
#     average = sum(numbers) / len(numbers)
#     return average
#
# average_1 = find_average(numbers)
# average_2 = find_average(numbers_1)
# print(average_1, average_2)
#
# print("----------------------------------------------------------------")
#
# def count_vowels(string):
#      VOLWELS = "aeioARTJFL"
#      count = 0
#      for char in string:
#          if char in VOLWELS:
#              count += 1
#      return count
#
# print(count_vowels("Hello World"))
# print(count_vowels("Python is powerfull language"))
#
# print("----------------------------------------------------------------")
#
# def nothing():
#     pass
#
#
# nothing()
#
# def format_date(day: int,month: str):
#     return f"the date is {day} of {month}"
#
# print(format_date(15,"October"))
#
#
# def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
#     return f"{greeting}, {name}"
#
# print(custom_greeting(name="Johan", greeting="Good mornining"))
# print(custom_greeting(name="Johan"))
#
# print("----------------------------------------------------------------")
#
# DEF_LVL_EXP = 200
#
#
# def is_lvl_up (*, current_exp: int , gained_exp: int) -> bool:
#     total_exp = current_exp + gained_exp
#     level_up = False
#
#     if total_exp >= DEF_LVL_EXP:
#         level_up = True
#
#     return level_up
#
# print(is_lvl_up(current_exp=150, gained_exp=60))
# print(is_lvl_up(current_exp=15, gained_exp=60))
#
# print("----------------------------------------------------------------")
# counter = 1
#
# while counter <= 5:
#     print(f"Counter is : {counter}")
#     counter += 1
#
#
# my_list = [0, 1, 2, 3, 4, 5]
#
# while my_list:
#     element = my_list.pop()
#     print(f"element: {element}")
#
# print(my_list)
#
# while True:
#     print("it is finish in yor list")
#
# while True:
#     answer = input("enter a number : ")
#     if answer == "quit":
#         break
#     print(f"You entered: {answer}")
# import random
#
# HEADS = "heads"
# TAILS = "tails"
# COIN_VAL = [HEADS, TAILS]
#
# def flip_coin():
#     return random.choice(COIN_VAL)
#
# def play_martingale(*, start_funds: int, min_bet: int, max_bet: int) -> int:
#     steps_to_loose = 0
#     current_funds = start_funds
#     current_bet = min_bet
#
#     while current_bet > 0:
#         steps_to_loose += 1
#         current_funds -= current_bet
#         if flipped_coin_valu == HEADS:
#             win
#
#
# user_roles = ("admin", "editor", "viewer")
#
# print("admin" in user_roles)
# print("writer" in user_roles)