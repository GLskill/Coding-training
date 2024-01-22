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
# ДЗ  сделать таблицу умнажения
#
rows = 6
columns = 6

multiP_table = ""

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        multiP_table += f"{i * j:3}"
    multiP_table += "\n"

print(multiP_table)


def table_of_multiplication(n):
    numbers = list(range(1, n + 1))

    result = ""
    for i in numbers:
        for j in numbers:
            result += f"{i} * {j} = {i * j}\t"
        result += "\n"

    return result

print(table_of_multiplication(9))