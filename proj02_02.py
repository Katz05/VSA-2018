# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
PreviousNumber = 0
CurrentNumber = 0
NextNumber = 1
Amount = int(raw_input("How many Fibonacci numbers would you like to generate?"))
for number in range(0,Amount):
    print NextNumber
    PreviousNumber = NextNumber
    NextNumber = CurrentNumber + PreviousNumber
    CurrentNumber = PreviousNumber