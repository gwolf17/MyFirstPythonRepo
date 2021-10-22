"""
Gillian Wolfersberger
Midterm 1
The purpose of the game is to randomly choose a song from a pre-defined list of 1980's songs
"""

import random

#CLASSES

class Person:
    #Constructor receives two string parameters and stores them to the firstName and lastName attributes of the class
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class Games:
    #Constructor receives integer parameter and assigns it to the guess_count attribute of the class
    def __init__(self, guess_count):
        self.guess_count = guess_count

#Inherits from Person class
class Contestant(Person):
    def __init__(self, firstName, lastName):
        #Call Person class constructor and pass firstName and lastName parameters
        super().__init__(firstName, lastName)
        self.number_of_games = 0
        self.games_played = []

    #Method to display game results
    def show_results (self):
        #Show if the player has not played any games
        if (self.number_of_games == 0):
            self.results = self.firstName + " " + self.lastName + " has not played a game."
        #Show if the player has played at least 1 game
        else:
            #Create empty variable to hold the number of total guesses made by the contestant
            self.total_guesses = 0
            #For loop to add up the total number of guesses the player made in each game
            for iCount in range(0,len(self.games_played)):
                self.total_guesses += self.games_played[iCount].guess_count
            #Add the total guesses to the output
            self.results = self.firstName + " " + self.lastName + " has played " + str(self.number_of_games) + " games and used a total of " + str(self.total_guesses) + " guesses."
        #Return the results stored in the self.results variable
        print(self.results)

#MAIN PROGRAM

#INITIALIZE VARIABLES
#List of songs users can choose from
listSongs = ["rocklobster", "peoplearepeople", "onceinalifetime", "sweetdreams", "missionaryman", 
"safetydance", "cars", "whipit"]
#Gather first and last name from user input
sFirstName = input("Enter your first name: ").title()
sLastName = input("Enter your last name: ").title()
#Initialize variable to check if the player wants to play again
sPlayAgain = 'Y'

#Make sure the user enters a first and last name before continuing
while (sFirstName == "" or sLastName == ""):
    sFirstName = input("You must enter your first name: ")
    sLastName = input("You must enter your last name: ")

#Create a new Contestant object using the above user inputs
oContestant = Contestant(sFirstName, sLastName)

#Loop for each game the player decides to play
while sPlayAgain == 'Y':
    #Keeps track of total guesses for a game
    iGuessCount = 0
    #Keeps track of the current guessed letter
    sGuessedLetter = ""
    #Keeps track of if the song name has been guessed or not
    sSongGuessed = False
    #Starting dictionary to keep track of the letters used (will be updated as the player uses letters)
    dictAlphabet = { 
    'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 
    'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 
    's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
    }

    #Determine the song title by choosing from the listSongs variable. Assign the random choice to a new variable
    sSongTitle = random.choice(listSongs)

    #Create a list to seperate out all the letters in the song title
    lstGuessSongTitle = list(sSongTitle)
    #Change the characters in the list to an underscore
    for iCount in range(0, len(lstGuessSongTitle)):
        lstGuessSongTitle[iCount] = "_"

    #Put the characters of the list back together and print the result to the user
    print(''.join(lstGuessSongTitle))

    #Create a new list to compare the player's guesses against the actual song title
    lstSongTitle = list(sSongTitle)

    #Make sure the guess count is less than 20
    while sSongGuessed == False:
        #Check to see if all of the letters have been correctly guessed
        if "_" not in lstGuessSongTitle:
            #If they have, print this statement and conclude this game
            print("Correct! You used " + str(iGuessCount) + " guesses\n" + "The song was " + sSongTitle)
            sSongGuessed = True
        #If the song has not been guessed, continue with the game
        else:
            #Don't let the player continue if they have made 20 guesses
            if iGuessCount > 19:
                print("You took too many guesses!")
                sSongGuessed = True
            else:
                #Let the player guess a letter
                sGuessedLetter = input("What letter do you want to guess? ")
                #Check to see if the letter has already been guessed by checking the value in the dictionary
                while dictAlphabet[sGuessedLetter] > 0:
                    sGuessedLetter = input("This letter has already been guessed. Please choose a different letter. ")
                #Check to see if the guessed letter is in the song title
                if sGuessedLetter in lstSongTitle:
                    #If it is, loop through the list and update the underscores to the correctly guessed letter
                    for iCount in range(0, len(lstSongTitle)):
                        if lstSongTitle[iCount] == sGuessedLetter:
                            #Update the list originally changed into all underscores
                            lstGuessSongTitle[iCount] = sGuessedLetter
                    #Print the updated list containing the correctly guessed letter(s) to the player
                    print(''.join(lstGuessSongTitle))
                #Print if the guessed letter is not in the song name
                else:
                    print("There is no", sGuessedLetter, "in the song name.")
                #Update the dictionary
                dictAlphabet[sGuessedLetter] = 1
            #Increment the Counter
            iGuessCount += 1

    #Create a Games object for the game just played and add it to the oContestant list attribute games_played
    oContestant.games_played.append(Games(iGuessCount))

    #Update the number of games played
    oContestant.number_of_games += 1

    #Check to see if the player wants to play again
    sPlayAgain = input("Do you want to play again? (Y/N): ").upper()
    #Correct variable in case user inputs "yes" instead of just "y"
    if sPlayAgain == "YES":
        sPlayAgain = "Y"

#Display game results for player
oContestant.show_results()