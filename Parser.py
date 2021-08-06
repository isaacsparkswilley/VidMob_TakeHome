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
    opRegex = re.compile('[\+\-\*\/]')

    '''
    DESC: Parse input string into a list of numbers and operators.
    IN: (String) Input from calculator CLI
    OUT: (List) List of seperated numbers and operators
    '''
    @staticmethod
    def parseInput(inputString):
        numRegex = Parser.numRegex
        opRegex = Parser.opRegex

        # output list
        out = []

        while inputString != '':
            # get next number
            match = re.match(numRegex, inputString)
            if match is not None:
                # cast number to float, add to out
                out.append(float(match.group()))
                # remove number from inputString
                inputString = inputString.replace(match.group(), "", 1)
            else:
                raise SyntaxError()

            # get next operator
            match = re.match(opRegex, inputString)
            if match is not None:
                # add operator to out
                out.append(match.group())
                # remove operator from input string
                inputString = inputString.replace(match.group(), "", 1)
            elif inputString != '':
                raise SyntaxError()

        return out
