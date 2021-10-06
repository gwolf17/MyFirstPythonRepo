# Gillian Wolfersberger
# This program

import random
from typing import IO

#Create team class
class Team:
    def __init__ (self, team_name):
        self.name = team_name
        self.wins = 0
        self.losses = 0

#input team name and convert to upper case
steam_name = input("Enter the team's name: ").upper()

#Create a new team object with the team name the user entered
oTeam = Team(steam_name)

#Initialize variables for number of games and output
iNumGames = 0
sOutput = ""

#Make sure they enter a number that is greater than 0
iNumGames = int(input("Enter the number of games played: "))
while (iNumGames == 0):
    print("Number of games cannot be 0.")
    iNumGames = int(input("Enter the number of games played: "))

#Use this list as the possible values of points for each quarter
listPoints = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
             7, 7, 7, 7, 7, 7, 7, 7, 7,  7, 7, 7, 7, 7, 7, 7, 7, 7, 
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             14, 14, 14, 14, 14, 14,
             21, 21,
             28]

#Use a for loop to play the number of games
for iCount in range(1, iNumGames + 1):
    #Initialize your score, opponent score, and overtime count
    iScore = 0
    iOpponentScore = 0
    iOvertime = 0
    #Get the opponent team name
    sOpponentName = input("Enter the Opponent's team name: ").upper()
    #Play 4 quarters of football
    for iQuarter in range(0,4):
        #Generate a random number using random.choice and use this for your score and the opponent score
        iScore += random.choice(listPoints)
        iOpponentScore += random.choice(listPoints)
    #If there is a tie, keep generating random numbers and adding them to your score and update the overtime count
    while (iScore == iOpponentScore):
        iOvertime += 1
        iScore += random.randrange(0,10)
        iOpponentScore += random.randrange(0,10)
    #Determine who won and update the wins and losses
    if (iScore > iOpponentScore):
        oTeam.wins += 1
    else:
        oTeam.losses += 1
    #Update the string output to be displayed and concatenate the number of overtimes if there were any
    if (iOvertime > 0):
        sOutput += oTeam.name + "-" + str(iScore) + " and " + sOpponentName + "-" + str(iOpponentScore) + " with " + str(iOvertime) + " overtime(s)\n"
    else:
        sOutput += oTeam.name + "-" + str(iScore) + " and " + sOpponentName + "-" + str(iOpponentScore) + "\n."

#Display results
print("\n", oTeam.name, "has a record of", oTeam.wins, "wins and", oTeam.losses, "losses\nHere are the games and scores:\n", sOutput)