#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: mhamilton-edwards

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Testing the function with various operations
    print(operate(10, 5, 'add'))        # Will return 15
    print(operate(10, 5, 'subtract'))   # Will return 5
    print(operate(10, 5, 'multiply'))   # Will return 50
    print(operate(10, 5, 'divide'))     # Will return error message
