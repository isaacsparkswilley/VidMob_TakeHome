'''
VidMob Take-Home Main Script
Isaac Sparks-Willey
August 9, 2021

This is the main script for running the calculator program.
'''
from Parser import *
from Calculator import *

# main loop
while True:
    # get user input
    inputString = input("Please enter an operation to be performed. (Exit to exit program)\n")

    # exit program on "exit" input
    if inputString.lower() == 'exit':
        break

    # attempt to parse inputString
    try:
        inputList = Parser.parseInput(inputString)

    # print syntax errors (malformed input)
    except SyntaxError as e:
        print(str(e) + "\n")
        continue

    # attempt to calculate result
    try:
        result = Calculator.calculate(inputList)

    # catch divide by zero errors
    except ZeroDivisionError:
        print("Unable to divide by zero.\n")
        continue

    # print result
    print("Result: " + str(result) + "\n")
