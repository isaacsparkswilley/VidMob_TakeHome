# VidMob_TakeHome - Isaac Sparks-Willey

This program is Isaac Sparks-Willey's solution to VidMob's Take Home exercise. The goal of the exercise is to create a calculator program, which takes a string (such as `'5+5'` or `'2*3/5'`) and outputs the result of the input operation.

## Prerequisites
Prior to running the VidMob Take Home calculator program, Python 3 must be installed.

## Usage
To use the calculator program, run `Main.py` via a CLI, IDLE, or your IDE of choice.

### Valid Syntax
The calculator program allows the following (strictly in this order):  
1. Optional open parenthesis `(`
2. A negative or positive number, with or without a decimal point (defined by the following regular expression:  
 `-?(?:\d*\.\d+|\d+)`)
3. Optional close parenthesis `)`
4. An operator (`+`, `-`, `*`, or `/`) Note: an operator is not required following the last number or parenthesis in the input string  
  
Any amount of whitespace (spaces, tabs, and newlines) will not affect the result.

## Testing
THe calculator program was thoroughly tested using a variety of test cases. To see these cases and their results, run the file `Test.py`. In addition to the test cases provided by VidMob, a variety of other test cases were created to fully test the program. The specific situations tested in `Test.py` are outlined here.

### Addition and Subtraction
- Basic addition
- Basic subtraction
- Addition followed by subtraction
- Subtraction followed by addition

## Multiplication and Division
- Basic multiplication
- Basic division
- Division resulting in a decimal answer
- Multiplication followed by division
- Division followed by multiplication

## Order of Operations and Parentheses
- Addition followed by multiplication
- Addition in parentheses followed by multiplication
- Multiplication followed by addition
- Multiplication followed by addition in parentheses
- Addition in parentheses divided by multiplication in parentheses
- Addition followed by nested parentheses: addition in parentheses followed by division
- Addition followed by nested parentheses: subtraction followed by multiplication in parentheses

## Negative Numbers and Decimals
- Addition of two decimals
- Subtracting a decimal negative number from a positive whole number
- Adding two negative numbers

## Spacing
- Addition with spaces present
- Addition with newlines present
- Addition with tabs present
- Addition with spaces, newlines, and tabs present

## Invalid input
- Multiple operators in a row
- Invalid numbers
- Random characters
- Operator other than `-` before the first number
- Unclosed open parenthesis
- Unopened close parenthesis
