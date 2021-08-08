'''
VidMob Take-Home Calculator Class
Isaac Sparks-Willey
August 5, 2021
'''

import operator
class Calculator:
    '''
    Calculator

    This class is used to calculate a value based on the output of the parser.

    Class Variables
    ---------------
    ops : {str : function}
        Dictionary mapping operator strings to operator functions

    Static Methods
    --------------
    calculate(inputList, containsParentheses=True)
        Calculate a number based on output of parser.
    calculateParens(inputList)
        Perform all calculations within parentheses, modifying the list of numbers and operators in place.
    calculateByOperators(inputList, opString)
        Perform all operations in inputList using operators defined by opString.
    '''

    ops = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }

    @staticmethod
    def calculate(inputList, containsParentheses=True):
        '''
        Calculate a number based on output of parser.

        Parameters
        ----------
        intputList : List
            List of separated numbers and operators
        containsParentheses : bool, optional (default True)
            Whether or not the list contains parentheses

        Returns
        -------
        out : float
            Result after calculation.
        '''
        
        # First, perform all calculations in parentheses if present
        if containsParentheses:
            Calculator.calculateParens(inputList)
        
        # Next, perform all multiplication and division
        Calculator.calculateByOperators(inputList, '*/')
        
        # Next, perform all addition and subtraction
        Calculator.calculateByOperators(inputList, '+-')

        # After all calculations, only result should remain in list
        if len(inputList) == 1:
            return inputList[0]
        else:
            raise SyntaxError("Incorrectly formatted list passed to Calculator.calculate().")

    @staticmethod
    def calculateParens(inputList):
        '''
        Perform all calculations within parentheses, modifying the list of numbers and operators in place.

        Parameters
        ----------
        inputList : List
            List of separated numbers and operators

        Returns
        -------
        N/A
        '''
        
        # stack to store indices of open parens
        openParens = []

        # find all open parentheses in inputList
        for i,v in enumerate(inputList):
            if v == '(':
                openParens.append(i)

        # while there are still open parens
        while openParens:
            openParenIndex = openParens.pop()
            
            # initialize closeParenIndex (a close paren is guaranteed to be found after parsing)
            closeParenIndex = -1
            
            # find first close paren after openParenIndex
            for i,v in enumerate(inputList[openParenIndex+1:]):
                if v == ')':
                    closeParenIndex = openParenIndex + 1 + i
                    break

            # calculate result within parentheses
            innerResult = Calculator.calculate(
                inputList[openParenIndex+1:closeParenIndex], containsParentheses=False)

            # replace openParen with result
            inputList[openParenIndex] = innerResult

            # delete through close paren
            for _ in range(openParenIndex, closeParenIndex):
                del inputList[openParenIndex+1]
            
        
    @staticmethod
    def calculateByOperators(inputList, opString):
        '''
        Perform all operations in inputList using operators defined by opString.

        Parameters
        ----------
        inputList : List
            List of separated numbers and operators, containing no parentheses
        opString  : str
            A string containing all operators that should be used in this pass of the list (eg '*/')

        Returns
        -------
        N/A
        '''
        
        # index in list
        i = 0
        
        while i < len(inputList):
            # if we are on an operator
            if isinstance(inputList[i], str) and inputList[i] in opString:

                # perform operation
                result = Calculator.ops[inputList[i]](inputList[i-1], inputList[i+1])
                
                # replace first number with result
                inputList[i-1] = result
                
                # delete operator and second number from list
                for _ in range(0,2):
                    del inputList[i]
                    
            # otherwise, we are not on an operator in opString
            else:
                i += 1
                
