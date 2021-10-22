class Team:
    def __init__(self, TeamName):
        self.TeamName = TeamName

    def retrieveContents(self):
        return self.TeamName

    def changeContents(self):
        self.TeamName = input("What is the team name?")

class SocerTeam(Team):
    def __init__ (self, TeamName, Wins, Losses, Draws):
        super().__init__(TeamName)
        self.Wins = Wins
        self.Losses = Losses
        self.Draws = Draws
        self.players = []

class Person:
    def __init__ (self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def retrieveName(self):
        self.sName = self.lastName + ", " + self.firstName
        return self.sName

    def changeName(self):
        self.firstName = input("Enter first name: ")
        self.lastName = input("Enter last name: ")

class Players(Person):
    def __init__ (self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.goalsScored = 0

    def accessScore(self):
        return self.goalsScored

    def setScore(self):
        self.goalsScored = int(input("How many goals were scored? "))

#Main program
iTeams = int(input("How many teams do you want to enter? "))

#Empty list to hold socer team objects
lstSocerTeams = []

#Loop to gather inputs and create socer team objects
for iOuter in range(0, iTeams):
    sTeamName = input("Enter the team name: ")
    iWins = int(input("How many wins? "))
    iLosses = int(input("How many losses? "))
    iDraws = int(input("How many draws? "))
    lstSocerTeams.append(SocerTeam(sTeamName, iWins, iLosses, iDraws))

    iPlayers = int(input("How many players does the team have? "))

    #Inner loop to gather inputs and create player objects which are stored in the players attribute of the socer team class
    for iInner in range(0,iPlayers):
        sFirstName = input("Player " + str(iInner + 1) + "'s first name: ")
        sLastName = input("Player " + str(iInner + 1) + "'s last name: ")
        #Having issues with this line of code
        lstSocerTeams[iInner].players.append(Players(sFirstName, sLastName))

#Print results using for loops
for iCount in range(0, iTeams):
    sTeamOutput = lstSocerTeams[iCount].retrieveContents() + " had a record of " + lstSocerTeams[iCount].Wins + "-" + lstSocerTeams[iCount].Losses
    print(sTeamOutput)
    for iInner in range(0,sTeamOutput[iCount].len(players))
    sPlayerOutput = lstSocerTeams[iCount].players[iCount].retrieveName()