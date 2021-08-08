'''
VidMob Take-Home Test Script
Isaac Sparks-Willey
August 6, 2021

This script contains a variety of test cases to test the calculator program.
'''

from Parser import *
from Calculator import *

# list of tuples where testCases[0] is the string to be tested and testCases[1]
# either the correct result of the calculation or None if test case is invalid
testCases = [
    # Vidmob supplied test cases
    ('1 + 2', 3),\
    ('4*5/2', 10),\
    ('-5+-8--11*2', 9),\
    ('-.32\t/.5', -0.64),\
    ('(4-2)*3.5',7) ,\
    ('2+-+-4', None),\
    ('19 + cinnamon', None),\
    # Addition / Subtraction
    ('2+2', 4),\
    ('4-2', 2),\
    ('2+2-4',0),\
    ('5-3+2',4),\
    # Multiplication / Division
    ('5*5', 25),\
    ('30/10', 3),\
    ('1/2', 0.5),\
    ('2*10/5', 4),\
    ('4/2*10', 20),\
    # Order of Operations / Parentheses
    ('2+5*5', 27),\
    ('(2+5)*5', 35),\
    ('2*2+4', 8),\
    ('2*(2+4)', 12),\
    ('(2+2)/(4*5)', 0.2),\
    ('2+((2+2)/2)', 4),\
    ('2+(5-(2*2))', 3),\
    # Negative Numbers / Decimals
    ('0.5+0.5', 1),\
    ('3--3.5', 6.5),\
    ('-2+-2', -4),\
    # Spacing
    ('2    +    2', 4),\
    ('3+\n3\n', 6),\
    ('5+\t5', 10),\
    ('3 . 5 +\n 3 \t+3\n', 9.5),\
    # Invalid Input
    ('2++2', None),\
    ('two + 2', None),\
    ('%^&*', None),\
    ('+2-2', None),\
    ('((8-5)', None),\
    ('(3+3))', None) ]

# iterate through each test case
for case in testCases:
    # print test case
    print("Test Case: " + case[0])

    # print expected result
    print("Expected Result: " + (str(float(case[1])) if case[1] is not None else "Error"))

    # attempt calculation, store "Error" as result if exception is thrown
    try:
        caseList = Parser.parseInput(case[0])
        result = Calculator.calculate(caseList)
    except:
        result = "Error"

    # print actual result
    print("Actual Result: " + str(result))

    # print successfulness and newline
    if case[1] is None and result == "Error":
        print("Success!")
    elif result == case[1]:
        print("Success!")
    else:
        print("Failure...")
    print()
