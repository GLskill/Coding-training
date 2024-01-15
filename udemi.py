# Section n1

print(2+3)
print(9-8)
print(4*6)
print(8/2)
print(5/2)
print(5//2)
print(8+9-10)
print((8+2)*5)
print(2*5*2)
print(2**5)
print(10//3)
print(10%3)
print("Navin skolko mozno bleat?")
print("Navin\'s laptop")

# Section n2

print("nums = 25,12,46,89,56")
print("nums[-1]")

# Creating a mutable list
my_list = [1, 2, 3, 4, 5]

# Modifying the list
my_list[2] = 10  # Changing the value at index 2
my_list.append(6)  # Appending a new element to the end
my_list.insert(1, 7)  # Inserting the value 7 at index 1

# Printing the modified list
print("Modified List:", my_list)

# Removing an element
removed_element = my_list.pop(3)  # Removing the element at index 3
print("Removed Element:", removed_element)
print("List after removal:", my_list)


# Creating a sequence (list)
my_list = [1, 2, 3, 4, 5]

# Iterating through the sequence
print("Sequence elements:")
for element in my_list:
    print(element)

# Slicing the sequence
sliced_portion = my_list[1:4]
print("\nSliced portion:", sliced_portion)

# Modifying the sequence
my_list[2] = 10  # Changing the value at index 2
my_list.append(6)  # Appending a new element to the end
my_list.insert(1, 7)  # Inserting the value 7 at index 1

# Printing the modified sequence
print("\nModified Sequence:", my_list)

# Removing an element
removed_element = my_list.pop(3)  # Removing the element at index 3
print("Removed Element:", removed_element)
print("Sequence after removal:", my_list)


import gc

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

# Creating objects
obj1 = MyClass("1")
obj2 = MyClass("2")

# Breaking reference cycles to trigger garbage collection
obj1 = None
obj2 = None

# Explicitly invoking garbage collection
gc.collect()
print("Garbage collection done.")

import gc

class NumericObject:
    def __init__(self, value):
        self.value = value
        print(f"NumericObject {self.value} created.")

# Creating numeric objects
obj1 = NumericObject(10)
obj2 = NumericObject(20)

# Breaking reference cycles to trigger garbage collection
obj1 = None
obj2 = None

# Creating more objects to show automatic garbage collection
obj3 = NumericObject(30)
obj4 = NumericObject(40)

# Letting Python's automatic garbage collection handle deallocation
print("Garbage collection happens automatically.")

# Explicitly invoking garbage collection (not recommended in normal scenarios)
gc.collect()
print("Garbage collection done.")


# Assigning numerical values to variables
num1 = 10
num2 = 5

# Performing numerical operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
remainder_result = num1 % num2
power_result = num1 ** num2

# Printing the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)
print("Power:", power_result)



# Getting input values from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing numerical operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
remainder_result = num1 % num2
power_result = num1 ** num2

# Printing the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)
print("Power:", power_result)


# Arithmetic operators
num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulo = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

# Comparison operators
is_equal = num1 == num2
not_equal = num1 != num2
greater_than = num1 > num2
less_than = num1 < num2
greater_than_or_equal = num1 >= num2
less_than_or_equal = num1 <= num2

# Logical operators
logical_and = (num1 > 0) and (num2 > 0)
logical_or = (num1 > 0) or (num2 > 0)
logical_not = not (num1 > 0)

# Assignment operators
result = 0
result += num1  # equivalent to result = result + num1
result -= num2  # equivalent to result = result - num2
result *= num1  # equivalent to result = result * num1
result /= num2  # equivalent to result = result / num2

# Membership operators
my_list = [1, 2, 3, 4, 5]
in_operator = 3 in my_list
not_in_operator = 6 not in my_list

# Printing the results
print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulo:", modulo)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)

print("\nComparison Operators:")
print("Equal:", is_equal)
print("Not Equal:", not_equal)
print("Greater Than:", greater_than)
print("Less Than:", less_than)
print("Greater Than or Equal:", greater_than_or_equal)
print("Less Than or Equal:", less_than_or_equal)

print("\nLogical Operators:")
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)

print("\nAssignment Operators:")
print("Result after operations:", result)

print("\nMembership Operators:")
print("In Operator:", in_operator)
print("Not In Operator:", not_in_operator)

from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 20

# Create Decimal numbers
decimal_num1 = Decimal('10.5')
decimal_num2 = Decimal('3.25')

# Perform arithmetic operations with Decimal
sum_result = decimal_num1 + decimal_num2
product_result = decimal_num1 * decimal_num2

# Convert Decimal to binary representation
binary_num1 = bin(int(decimal_num1))
binary_num2 = bin(int(decimal_num2))

# Print results
print("Decimal Numbers:")
print("Num1:", decimal_num1)
print("Num2:", decimal_num2)

print("\nArithmetic Operations:")
print("Sum:", sum_result)
print("Product:", product_result)

print("\nBinary Representation:")
print("Binary Num1:", binary_num1)
print("Binary Num2:", binary_num2)

# Decimal to Binary Conversion
decimal_num = 10
binary_representation = bin(decimal_num)

# Binary to Decimal Conversion
binary_num = '0b1010'
decimal_result = int(binary_num, 2)

# Printing results
print(f"Decimal to Binary: {decimal_num} to {binary_representation}")
print(f"Binary to Decimal: {binary_num} to {decimal_result}")

# Bitwise AND
num1 = 10    # Binary: 1010
num2 = 5     # Binary: 0101
result_and = num1 & num2

# Bitwise OR
result_or = num1 | num2

# Bitwise XOR
result_xor = num1 ^ num2

# Bitwise NOT
result_not_num1 = ~num1

# Left Shift
result_left_shift = num1 << 1

# Right Shift
result_right_shift = num1 >> 1

# Printing results
print(f"Bitwise AND: {num1} & {num2} = {result_and}")
print(f"Bitwise OR: {num1} | {num2} = {result_or}")
print(f"Bitwise XOR: {num1} ^ {num2} = {result_xor}")
print(f"Bitwise NOT: ~{num1} = {result_not_num1}")
print(f"Left Shift: {num1} << 1 = {result_left_shift}")
print(f"Right Shift: {num1} >> 1 = {result_right_shift}")

