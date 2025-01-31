#!/usr/bin/env python3

# Function that does not take arguments or return values
def hello():
    print('Hello World')
    print('Inside a Function')

# Calling the function three times
hello()
hello()
hello()

# Checking what happens when a function does not return anything
my_stuff = hello()
print('Stuff returned from hello():', my_stuff)
print('The object my_stuff is of type:', type(my_stuff))

# Function that returns  with a string
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

# calling  the function and keeping  the return value
text = return_text_value()
print(text)

# getting the Function that returns a number
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

# Calling the function and using the returned number
number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)

# the right  way to concatenate a number using  a string
print('my number is', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))

