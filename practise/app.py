# print('My name is Akshay, my age is', 34)
# print('Welcome')
#
# # Variables in Python
#
# name = 'Akshay'
# age = 18
# print(name + ' is a boy')
# print(name + ' is a boy and his age is ',age)
# print(name)
#
# # new line and break
# print('Hello World !!\nHow are you ?')
# print(name[0].lower())
# print(name[0].upper())
# # Length of a string
# print(len(name))
# # Get index of a string
# print(name.index('h'))
# # Replace
# print(name.replace('h','H'))
#
# # Number in Python
# number = 79
# print(78 + 22)
# print(78 + 22.100)
# print(number)
#
# # Getting users input
# name = input('Input your name: ')
# age = input('Input your age: ')
# print(name)
# print('Your Name is : ' + name + ' and your age is ' + age)
#
# User input and replace
# sentence = input("Enter a sentence: ")
# print('Your sentence is ' + sentence)
# word1 = input('Enter word to replace: ')
# word2 = input('Enter word to replace it with: ')
# print(sentence.replace(word1,word2))

# List Methods
# countries=['united kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']
# print(countries)
# print(countries[0])
# print(countries[2][0])
# print(countries[1:])
# print(countries[2:])
# print(countries[1:4])
# print(type(countries))
# print(type(countries[0]))
# print(type(countries[0][1]))
# countries[0] = 'United States'
# print(countries)
# print(countries[-1])
# print(len(countries))

# countries = list(('IND', 34, False))
# countries2 = ['a','b', 'c']
# countries.extend(countries2)
# print(countries)

# Tuples
# You cannot change a value in Tuple
# Tuple are immutable
# three_numbers = (1, 'Home', True, 3, 1)
# three_numbers_tuple = tuple((1, 'Home', True, 3, 1))
# print(three_numbers)

# Functions
# Syntax -> def name_of_function

# def greetings_function():
#     print('Welcome User')
#
# greetings_function()
#
# def greetings_function(name, age):
#     print('Welcome User', name)
#     print('You age : ' + str(age))
#
# greetings_function('John',34)
#
# def greetings_function(*name):
#     print('Welcome User', name[0])
#     print('You age : ' + str(name[1]))
#
# greetings_function('John',34)

# Return statements

# def my_function():
#     return 5+4
#
# print(my_function())

# if statement in Python
# a = 'Time'
# b = 'Tim'
#
# if a == b:
#     print('a == b')
# elif a == 'Time':
#     print('a is Time')
# else:
#     print('a != b')

# Dictionary
# my_dict = {
#     'name':'Tim',
#     'age':30,
#     'Nationality': 'Indian'
# }
#
# print(my_dict)
# print(my_dict['name'])

# while loop
# i = 1
# while i < 6 or i == 10:
#     print(i)
#     i += 1

# for i in range(0,7):
#     print(i)
# else:
#     print('i =',i)

# 2D list
# my_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
#
# for lists in my_list:
#     print(lists)
#
# for lists in my_list:
#     for item in lists:
#         print(item)

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
op = input("Enter operation : ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print('Invalid operation', op)

# Try Except