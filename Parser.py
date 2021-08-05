'''
VidMob Take-Home Parser Class
Isaac Sparks-Willey
August 5, 2021

This class is used to parse the calculator's CLI input, validating it's syntax
and converting the single line string into a list of numbers and operators.
'''
import re
class Parser:

    # regex to use for validating numbers
    numRegex = re.compile('-?(?:\d*\.\d+|\d+)')

    # regex to use for validating operators
    opRegex = re.compile('[\+\-]')

    '''
    DESC: Parse input string into a list of numbers and operators.
    IN: (String) Input from calculator CLI
    OUT: (List) List of seperated numbers and operators
    '''
    def parseInput(inputString):
        pass
