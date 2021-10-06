"""
Gillian Wolfersberger
This program determines win/loss percentages of teams based on user input
"""

#Gather number of teams from user
iNumTeams = int(input("Enter the number of teams: "))

#Set beginning win/loss percentage
fHighestPercentage = 0

#Loop for each team entered
for iOuter in range(1, iNumTeams +1, 1):
    #Declare variables
    iNumGames = 0
    iTeamScore = 0
    iOpponentScore = 0
    iWins = 0
    iLosses = 0
    fPercentage = 0
    #Determine team name
    sTeamName = input("Enter the team's name: ")
    #Determine number of games played by each team
    iNumGames = int(input("Enter the number of games played by team " + sTeamName + ": "))

    #Loop to determine scores for each game
    for iInner in range(1, iNumGames +1, 1):
        #Convert iInner to a string so as to be able to concatenate later
        sGameNumber = str(iInner)
        #Determine scores
        iTeamScore = int(input("Enter " + sTeamName + "'s score for game " + sGameNumber + ": "))
        iOpponentScore = int(input("Enter the opponent's score for game " + sGameNumber + ": "))
        #Don't allow ties
        if (iTeamScore == iOpponentScore):
            print("You cannont have a tie")
            iTeamScore = int(input("Enter " + sTeamName + "'s score for game " + sGameNumber + ": "))
            iOpponentScore = int(input("Enter the opponent's score for game " + sGameNumber + ": "))
        #Update iWins and iLosses variables
        if (iTeamScore > iOpponentScore):
            iWins += 1
        else:
            iLosses += 1
    
    #Determine win/loss percentage
    fPercentage = (iWins/iNumGames)

    #Determine if this team has the higher win/loss percentage
    if (fPercentage > fHighestPercentage):
        fHighestPercentage = fPercentage
        sBestTeam = sTeamName

#Print results
print(sBestTeam, "had the highest win/loss percentage of", fHighestPercentage)

