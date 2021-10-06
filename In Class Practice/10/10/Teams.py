"""
Gillian Wolfersberger
"""
import random

#Create team class
class Team : 
    #Constuctor
    def __init__ (self, team_name):
        self.team_name = team_name
        self.mascot = ""

    #Displays the team name and their mascot
    def display_info(self):
        return("\n\n" + self.team_name + " has a mascot of a " + self.mascot)

#Create Basket_Ball class
class Basket_Ball (Team) :
    #Constructor
    def __init__(self, sTeam_Name):
        super().__init__(sTeam_Name)
        self.wins = 0
        self.losses = 0

    #Calls the Team class method, diplay_info, and adds on the team's wins and losses
    def display_record(self):
        return("\n\n" + self.display_info() + "\nRecord: " + str(self.wins) + "-" + str(self.losses))


#Gather inputs from user and set variables
sTeam_Name = input("Enter the team's name: ").upper()
sOutput = "" #For the output of total wins and losses at the end

#Create a new team object with the team name the user entered
oTeam = Basket_Ball(sTeam_Name)

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
        #Generate a random number from the listPoints variable
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
        sOutput += oTeam.team_name + "-" + str(iScore) + " and " + sOpponentName + "-" + str(iOpponentScore) + " with " + str(iOvertime) + " overtime(s)\n"
    else:
        sOutput += oTeam.team_name + "-" + str(iScore) + " and " + sOpponentName + "-" + str(iOpponentScore) + "\n."

#Call display_record method from Basketball class and display results
sMethodOutput = oTeam.display_record()
print(sMethodOutput, "\nHere are the games and scores:\n", sOutput)