"""
Gillian Wolfersberger
This program generates two random numbers until they are not equal and then displays them
"""

"""Write a program that will continue to generate two random numbers until they are not equal. Then display the two numbers."""

#Import random functions
import random

#Allow user to input range max for random number generation
iMax = int(input("Enter the max number to use (must be greater than 1): "))

#Create variables to hold two random numbers
iNum1 = random.randrange(0,iMax)
iNum2 = random.randrange(0,iMax)

while (iNum1 == iNum2):
    iNum1 = random.randrange(0,iMax)
    iNum2 = random.randrange(0,iMax)

#Print results once numbers are not equal
print("First number:", iNum1, "\nSecond Number:", iNum2)