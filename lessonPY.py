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
#
# Словарь ( Dict )
#
# person = {
#     "name": "john",
#     "age": 30,
#     "city": "Now York",
#     "car": "Ford mustang GT"
# }
#
# person["job"] = "Engineer"
#
# official_information_info = {
#     "name": "Piter",
#     "age": 36,
#     "city": "Saint Petersburg",
#     "job": "Boilinger"
# }
#
# person =  person | official_information_info
#
# print(person)
#
# print("----------------------------------------------------------------")
#
# def add(x: int, y: int) -> int:
#     return x + y
#
# print(add(12, 23))
#
# def add_all(*args):
#     print(args)
#     print(type(args))
#
# add_all(1, 2, 4, 5, 6)
#
# def add_all(*args):
#     summary = 0
#     for num in args:
#         summary += num
#     return summary
#
# print(add_all(1, 2, 4, 5, 6))
#
# numbers_01 = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8 ,9]
# other_numbers = [12, 56, 23, 66]
#
# print(add_all(*numbers_01, *other_numbers))
#
#
# def introduce(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# introduce(name="Johan", age=56, city="Big apple")
#
# def func_with_all_arguments(x: int, y: int, *args, value: int = 6,**kwargs):
#     print(x, y)
#     print(args)
#     print(value)
#     print(kwargs)
#
# person = {
#     "name": "john",
#     "age": 30,
#     "city": "Now York",
#     "car": "Ford mustang GT"
# }
#
# func_with_all_arguments(1, 2, 3, 4, 5, **person)
#
#
# print("----------------------------------------------------------------")
# def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
#     is_modified = False
#
#     for key, value in kwargs.items():
#         if old_dict.get(key) != value:
#             old_dict[key] = value
#             is_modified = True
#
#     return old_dict, is_modified
#
# product = {'id': 1, 'name': 'Laptop', 'price': 19.999}
#
# product, wos_modified = modify_dict(old_dict=product, in_stock=True)
#
# print(product)
# print(wos_modified)
# print("----------------------------------------------------------------")
#
# import json
#
# book = {
#     'title': '1984',
#     'author': 'George Orwell',
#     'isbn': '978-0451524935',
#     'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
# }
#
# json_string = json.dumps(book)
#
# print(type(json_string))
# print(json_string)
#
# json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}'
#
# book = json.loads(json_string)
#
# look = book
#
# kekcheburek = look
#
# print(type(json_string))
# print(json_string)
# print("----------------------------------------------------------------")
#
#
# import requests
#
# response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'DOTUSDT'})
# content = response.content
# print(content)
# print(type(content))
# price_object = response.json()
# price = float(price_object['price'])
#
#
# import time
#
# bitcoin_prices = []
# for i in range(15):
#     response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'DOTUSDT'})
#     price = float(response.json()["price"])
#     price = round(price, 2)
#     bitcoin_prices.append(price)
#     time.sleep(1)
#
# print(bitcoin_prices)
# print(len(bitcoin_prices))
# print(max(bitcoin_prices))
# print(min(bitcoin_prices))
#
# print("----------------------------------------------------------------")
#
# import requests
#
# response = requests.get('https://api.binance.com/api/v3/ticker/price')
#
# for ticker in response.json():
#     if ticker['symbol'] == 'ETHUSDT':
#         print(ticker['price'])
#
#print("----------------------------------------------------------------")
#
# squares = []
# for x in range(20):
#     squares.append(x ** 2)
#
# print(squares)
#
# # ОДин и тот же способ
#
# squares_01 = [x ** 3 for x in range (15)]
#
# print(squares_01)
#
# even_squares = []
# for x in range(15):
#     if x % 2 == 0:
#         even_squares.append(x ** 2)
#
# print(even_squares)
#
# print("-----------------------------------------------------------------")
#
# even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
#
# print(even_squares)
#
# labelled_numbers = []
# numbers = (1, 2, 4, 5, 6, 7, 9)
#
# for num in numbers:
#     if num % 2 == 0:
#         labelled_numbers.append("even")
#     else:
#         labelled_numbers.append("odd")
#
# print(labelled_numbers)
#
# print("-----------------------------------------------------------------")
#
# labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
#
# print(labelled_numbers)
#
# square_dict = {x: x ** 2 for x in range(20)}
# print(square_dict)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8 ,9]
# ]
#
# transpose_matrix = []
#
# for i in range(len(matrix)):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)
#
# print(transpose_matrix)
#
# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
#
# print(transpose_matrix)
#
# my_set = {1, 2, 3, 4, 5, 6, 7}
#
# print(type(my_set))
# print(my_set)
#
# my_set_01 = set()
#
# for i in range(10):
#     my_set_01.add(i)
#
# print(my_set_01)
#
# my_set = {1, 2, 3, 4, 5}
#
# print(type(my_set))
# print(my_set)
#
# my_set = set()
# for i in range(5):
#     my_set.add(i)
# print(my_set)
#
# my_set = {0, 1, 2, 3, 4}
# my_set.add(2)
# print(my_set)
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# print(set1.union(set2))
# print(set1.intersection(set2))
# united_set = set1.union(set2)
# print(len(united_set))
# print(set1.difference(set2))
#
# squares = {x ** 2 for x in range(10)}
# print(squares)
#
# print({1, 2, 3} == {3, 2, 1})
# my_set = {1, 2, 3}
#
# numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
# unique_numbers = set(numbers)
# print(unique_numbers)
# unique_numbers = list(unique_numbers)
# print(unique_numbers)
#
# unique_numbers = list(set(numbers))
# print(unique_numbers)
#
# print("-----------------------------------------------------------------")
#
# fruits = ['banana', 'apple', 'cherry', 'date']
# sorted_fruits = sorted(fruits)
# sorted_fruits_01 = sorted(fruits,reverse=True)
#
#
# print(sorted_fruits)
# print(fruits)
# print(sorted_fruits_01)
#
# def sort_by_len(element: str) -> int:
#     return len(element)
#
# print(sort_by_len)
# print(type(sort_by_len))
#
# sorted_fruits = sorted(fruits, key=sort_by_len)
#
# print(sorted_fruits)
#
#
# def sort_by_age(element):
#     return element["age"]
#
#
# sorted_people = sorted(people, key=sort_by_age)
# print(sorted_people)
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Diana", "age": 30},
#     {"name": "Charlie", "age": 30},
# ]
#
#
# def sort_by_age_name(element):
#     return element["age"], element["name"]
#
#
# sorted_people = sorted(people, key=sort_by_age_name)
# print(sorted_people)
#
# print("-----------------------------------------------------------------")
#
# def is_even(n: int) -> bool:
#     return n % 2 == 0
#
# numbers = [10, 11, 12, 14, 15, 16]
#
# filtered_numbers = list(filter(is_even, numbers))
#
# print(type(filtered_numbers))
# print(filtered_numbers)
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Diana", "age": 30},
#     {"name": "Charlie", "age": 30},
# ]
#
# def is_adult(person: dict) -> bool:
#     return person["age"] >= 22
#
# filter_people = list(filter(is_adult,people))
# print(filter_people)
#
#
# def sort_by_len(element: str) -> int:
#     return len(element)
#
#
# sort_by_len_lambda = lambda element: len(element)
# print(sort_by_len("banana"))
# print(sort_by_len_lambda("banana"))
#
#
# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits, key=lambda element: len(element))
#
# fruits = ["apple", "banana", "cherry", "date"]
# longest_word = max(fruits, key=lambda x: len(x))
# print(longest_word)
#
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Charlie", "age": 20},
#     {"name": "Bob", "age": 20},
#     {"name": "Diana", "age": 30},
# ]
# people_min = min(people, key=lambda x: (x["age"], x["name"]))
# print(people_min)
#
# print("-----------------------------------------------------------------")
#
# def find_average(*, numbers: list) -> float:
#     return  sum(numbers) / len(numbers)
#
# try:
#     print(find_average(numbers=[1, 2, 3, 5, 6, 7,]))
# except ZeroDivisionError:
#     print("the list is empty")
#
# print("-----------------------------------------------------------------")





