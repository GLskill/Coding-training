list = [4,5,9,12,5,54,34,3,12,12,99]
print(list)
index = 0

print(f"element by index:{index}")
print(list[index])

uniq = set(list)
print(f"uniq elements from:{list}")
print(uniq)

def custom_print(my_value):
     print(my_value)

print("-----------------------------------------------")

print(uniq)
custom_print(uniq)

def delimetr_my():
    print("-----------------------------------------------")

def make_set_and_print(my_list, count):
    print(my_list)
    print(count)
    delimetr_my()
    for _ in range(count):
        delimetr_my()
        print(set(my_list))
        print(range(count))
        delimetr_my()



delimetr_my()
custom_print("uniq")

make_set_and_print(my_list=list, count=5)

