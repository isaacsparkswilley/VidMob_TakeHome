'''
VidMob Take-Home Parser Class
Isaac Sparks-Willey
August 5, 2021
'''

import re
class Parser:
    '''
    Parser
    
    This class is used to parse the calculator's CLI input, validating it's syntax and converting the string
    into a list of numbers and operators.

    Class Variables
    ---------------
    numRegex : str
        regex to use for validating numbers
    opRegex : str
        regex to use for validating operators
    openParenRegex : str
        regex to use for validating open parentheses
    closeParenRegex : str
        regex to use for validating close parentheses

    Static Methods
    --------------
    parseInput(inputString)
        Parse input string into a list of numbers and operators, raising SyntaxError if formatted incorrectly.
    '''

    numRegex = re.compile('-?(?:\d*\.\d+|\d+)')
    opRegex = re.compile('[\+\-\*\/]')
    openParenRegex = re.compile('[\(]')
    closeParenRegex = re.compile('[\)]')

    @staticmethod
    def parseInput(inputString):
        '''
        Parse input string into a list of numbers and operators.

        Parameters
        ---------
        inputString : str
            Input from calculator CLI

        Returns
        -------
        out : List
            List of separated numbers and operators
        '''
        
        # output list
        out = []

        # number of parentheses that have been opened but not closed
        openParens = 0

        # remove whitespace from inputString
        inputString = "".join(inputString.split())

        while inputString != '':
            # get open parens (which will always come before a number)
            match = re.match(Parser.openParenRegex, inputString)
            
            while match is not None:
                # note number of opened parentheses
                openParens += 1
                
                # add paren to out
                out.append(match.group())
                
                # remove paren from inputString
                inputString = inputString.replace(match.group(), "", 1)
                
                # check for another paren
                match = re.match(Parser.openParenRegex, inputString)

            # get next number
            match = re.match(Parser.numRegex, inputString)
            
            if match is not None:
                # cast number to float, add to out
                out.append(float(match.group()))
                
                # remove number from inputString
                inputString = inputString.replace(match.group(), "", 1)

            else:
                raise SyntaxError("Invalid Input")

            # get close parens (which will always come after a number)
            match = re.match(Parser.closeParenRegex, inputString)
            
            while match is not None:
                # note number of closed parentheses
                openParens -= 1
                
                # add paren to out
                out.append(match.group())
                
                # remove paren from inputString
                inputString = inputString.replace(match.group(), "", 1)
                
                # check for another paren
                match = re.match(Parser.closeParenRegex, inputString)

            # get next operator
            match = re.match(Parser.opRegex, inputString)
            
            if match is not None:
                # add operator to out
                out.append(match.group())
                
                # remove operator from input string
                inputString = inputString.replace(match.group(), "", 1)
                
            elif inputString != '':
                raise SyntaxError("Invalid Syntax")

        # ensure evenly placed parentheses
        if openParens != 0:
            raise SyntaxError("Mismatched Parentheses")
        
        return out
