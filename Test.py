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
    ('1 + 2', 3),\
    ('4*5/2', 10),\
    ('-5+-8--11*2', 9),\
    ('-.32\t/.5', -0.64),\
    ('2+-+-4', None),\
    ('19 + cinnamon', None),\
    ('(4-2)*3.5',7) ,\
    ('((4-2)*3.5)',7)]

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
