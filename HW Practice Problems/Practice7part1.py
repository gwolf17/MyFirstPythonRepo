"""
Gillian Wolfersberger
This program generates a random number (range max based on user input) and times how long it takes the user to guess the number
"""

#Import random and datetime functions
import random
from datetime import datetime

#Get max number from user
iMax = int(input("Enter any number greater than 1: "))

#Generate random number
iRandom = random.randrange(0, iMax)

#Begin timer and allow user to start guessing the number
dStart = datetime.now()
iGuess = int(input("Enter your guess: "))

while (iGuess != iRandom):
    if (iGuess > iRandom):
        print("Too high!")
    else:
        print("Too low!")
    iGuess = int(input("Enter your guess: "))

#Record time when user guesses the number
dEnd = datetime.now()

#Determine how long it took the user to guess the correct number
dResult = dEnd - dStart
print("It took you", dResult.seconds, "seconds to correctly guess the number.")