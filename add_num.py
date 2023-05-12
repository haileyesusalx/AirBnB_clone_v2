#!/usr/bin/python3
# add two numbers

import sys


def add_num(num1, num2):
    result = num1 + num2
    return result


if __name__ == '__main__':
    # Get number arguments from the terminal
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    # Call the add_num function with the number arguments
    result = add_num(num1, num2)

    # Print the result
    print(result)
