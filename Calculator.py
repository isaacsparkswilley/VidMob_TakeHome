'''
VidMob Take-Home Calculator Class
Isaac Sparks-Willey
August 5, 2021

This class is used to calculate a value based on the output of the parser.
'''
import operator
class Calculator:

    '''
    DESC: Calculate a number based on output of parser.
    IN: (List) List of seperated numbers and operators
    OUT: (Float) Result after calculation.
    '''
    @staticmethod
    def calculate(inputList):
        # First, perform all calculations in parentheses
        Calculator.calculateParens(inputList)
        
        # Next, perform all multiplication and division
        Calculator.calculateByOperators(inputList, '*/')
        
        # Next, perform all addition and subtraction
        Calculator.calculateByOperators(inputList, '+-')

        # After all calculations, only result should remain in list
        if len(inputList) == 1:
            return inputList[0]
        else:
            # Throw error

    '''
    DESC: Perform all calculations within parentheses, modifying the list of numbers and operators in place.
    IN: (List) List of seperated numbers and operators
    OUT: N/A - List is modified in place, replacing everything from opening paren to close paren with result of
                calculation
    '''
    @staticmethod
    def calculateParens(inputList):
        pass

    '''
    DESC: Perform all operations in inputList using operators defined by opString.
    IN: (String) A string containing all operators that should be used in this pass of the list
    OUT: N/A - List is modified in place, replacing all numbers an operators with result of calculation
    '''
    @staticmethod
    def calculateByOperators(inputList, opString):
        pass
