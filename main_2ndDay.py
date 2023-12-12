
#! Variables
# name = "Beau"
# age = 24
# print(isinstance(name, str))

#! Casting. Convert string to number. Convert number to string
# number = "20"
# age = int(number)
# print(isinstance(age, int))
#int to string and string to int
# ageString = "34"
# ageInt = int(ageString)
# age = str(39)
# print(isinstance(ageInt, int))

#! Arithmetic Operators 
#*Addition
# _addition = 1 + 1

#*Subtraction
# _subtract = 2 - 1

#*Multiplication
# _multi = 2 * 2

#*Division
# _division = 4 / 2

#*Remainder
# _remainder = 4 % 3

#*square root
# _toThePower = 4 ** 2

#*Floor division, Rounds down
# _floorDivision = 4 // 2

# print(f" Addition = {_addition},\n Subtraction = {_subtract},\n Multiplication{_multi},\n Division = {_division},\n Remainder = {_remainder},\n Square Root = {_toThePower},\n Floor Division = {_floorDivision}")
#!Comparison Operators
# a == b
# a != b
# a > b
# a < b
# a >= b
# a <=b
#! Boolean Operators 
#* 'or', it returns the 1st condition that is equal to TRUE, if the 1st condition is false it will check the other condition and if it still false it will return the last value of condition
# print("\n 'or' operator")
# print(0 or 1)
# print(False or 'hey')
# print('hi' or 'hey')
# print([] or False)
# print(False or [])

#* 'and', only evaluates the 2nd condition if the first condition is true, if the 1st condition is false it will return the value of the 1st condition.
# print("\n 'and' operator")
# print(0 and 1)
# print(1 and 0)
# print(False and 'hey')
# print('hi' and 'hey')
# print([] and False)
# print(False and [])

#!Bitwise operators
# Bitwise operators are rarely used in real life situations. 
#* '&' performs binary AND
#* '|' performs binary OR
#* '^' performs a binary XOR operation
#* '~' performs a binary NOT operation
#* '<<' shift left operation
#* '>>' shift right operation

#* 'is' this is an identity operator, it used to compare objects and returns true if both are the same objects.

#* 'in' this is an membership operator, this is used to tell a value is contained in a list or on another sequence.

#! Ternary Operator
# instead of this long code, we can simplify this by using ternary operator.
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False

#example of ternary operator
# def is_adult2(age):
#     return True if age >= 18 else False
        
#! String concatenation
# name  = "Beau"
# name += "is my name"
#* Multi line string
# print(f"""Beaus is  
# {name}
# is 39
# yrs old
# """)

#! String methods
#* list of string methods or properties
# isalpha() to check if a string contains only characters and is not empty
print("a".isalpha())

# isalnum() to check if a string contains characters or digits and is not empty
num = "1"
print(num.isalnum())

# isdecimal() to check if a string contains digits and is not empty
age = 25
print(str(age).isdecimal())

# lower() to get a lowercase version of a string
print("LOWER".lower())

# islower() to check if a string is lowercase
print("lower".islower())

# upper() to get an uppercase version of a string
print("UPPER".upper())

# isupper() to check if a string is uppercase
print("UPPER".isupper())

# title() to get capitalized version of a string
print("my name is mark parayno".title())

# startswith() to check if the string starts with a specific substring
intro = "Hi my name is mark parayno"
print(intro.startswith("H"))
print(intro.startswith("my"))
print(intro.startswith("i",1,9))

# endswith() to check if the string ends with a specific substring
print(intro.endswith("o"))
print(intro.endswith("Mark Parayno"))
print(intro.endswith("m"  , 14, 26))

# replace() to replace a part of string
name = "mark"
print(name.replace("mark", "philip"))

# split() to split a string on a specific character separator
char = "character"
print(char.split("ter"))

# strip() to trim the whitespace from a string
x = "mark".strip()
print(f"my name is          {x}           parayno")

# join() to append new letters to a string
join = "mark"
print(join.join("TTT"))

# find() to find the position of a substring
print(intro.find("mark"))
