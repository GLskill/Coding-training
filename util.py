# import random
#
# def flip_coin(COIN_VAL):
#     return random.choice(COIN_VAL)
#
# test = "HellO WorLD"
# expected = "hello world"
# assert test in expected
# print("------------------------------")
# assert test.lower() in expected

my_list = [1, 4, 5, 7, 98, 286]
for element in my_list:
    if element == 1:
        my_list.remove(element)
print(my_list)


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