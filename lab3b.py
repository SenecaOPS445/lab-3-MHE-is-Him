#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: mhamilton-edwards 

def sum_numbers(number1, number2):
    # Add number1 and number2 and return the value
    return number1 + number2

def subtract_numbers(number1, number2):
    # Subtract number2 from number1 and return the value
    return number1 - number2

def multiply_numbers(number1, number2):
    # Multiply number1 and number2 and return the value
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))  # Will return 15
    print(subtract_numbers(10, 5))  # Will return 5
    print(multiply_numbers(10, 5))  # Will return 50

