class Team() :
    number_of_teams = 0

    def __init__ (self, sTeam_Name) :
        self.team_name = sTeam_Name
        self.mascot = ""
        Team.number_of_teams += 1

    def display_info(self) :
        return ("\n\n" + self.team_name + " has a mascot of a " + self.mascot)

class Basketball_Team(Team) :
    def __init__ (self, sTeam_Name) :
        super().__init__ (sTeam_Name)
        self.wins = 0
        self.losses = 0
    
    def display_record(self) :
        return (self.display_info() + "\n" + " Record: " + 
                    str(self.wins) + " - " + str(self.losses))

listPoints = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
             7, 7, 7, 7, 7, 7, 7, 7, 7,  7, 7, 7, 7, 7, 7, 7, 7, 7, 
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             14, 14, 14, 14, 14, 14,
             21, 21,
             28]

import random

#input team name and convert to upper case
sTeam = input("Enter Team Name: ").upper()

oTeam = Basketball_Team(sTeam) 
oTeam.mascot = "Cougar"

#initialize variables for number of games, output, wins, and losses
iGames = 0
sOutput = ""

#Make sure they enter a number that is greater than 0
while (iGames <= 0) :
    try :
        iGames = int(input("\nHow many games? "))
    except :
        print("Enter a number")

#Use a for loop to play the number of games
for iGameCount in range(1, iGames + 1) :
    #Initialize your score, opponent score, and overtime count
    iMyScore = 0
    iOpponentScore = 0
    iOverTime = 0

    #Get the opponent team name
    sOpponent = input("\nEnter Opponent Name: ").upper() 

    #Play 4 quarters of football
    for iQuarter in range(0, 4) :
        #Generate a random number using random.choice and use this for your score and the opponent score
        iMyScore = iMyScore + random.choice(listPoints)
        iOpponentScore = iOpponentScore + random.choice(listPoints)

    #If there is a tie, keep generating random numbers and adding them to your score and update the overtime count
    #Make sure you update the wins and losses
    while (iMyScore == iOpponentScore) :
        iMyScore = iMyScore + random.choice(listPoints)
        iOpponentScore = iOpponentScore + random.choice(listPoints)            
        iOverTime += 1

    #Determine who won and update the wins and losses
    if (iMyScore > iOpponentScore) :
        oTeam.wins += 1
    else :
        oTeam.losses += 1

    #Update the string output to be displayed showing:
    #Your Team name-score and Opponent name-score
    #For example: BYU-26 and UTAH-17
    sOutput = sOutput + oTeam.team_name + "-" + str(iMyScore) + " and " + sOpponent + "-" + str(iOpponentScore)

    #Concatenate the number of overtimes if there were any
    #For example: BYU-26 and UTAH-17 with 1 overtimes
    if (iOverTime > 0) :
        sOutput = sOutput + " with " + str(iOverTime) + " overtimes"
    
    #Make sure the output uses whitespace to make it more readable
    sOutput = sOutput + "\n"

print(oTeam.display_info())
print("\nHere are the games and scores:\n")
print(sOutput)

if (Team.number_of_teams == 1) :
    print("There is " + str(Team.number_of_teams) + " team")
else :
    print("There are " + str(Team.number_of_teams) + " team")