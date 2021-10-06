"""
Gillian Wolfersberger
This program asks for a user's name, address, and birth year.
Age is determined and results are printed.
"""

#Gather inputs and assing to variables
sFirstName = input("Enter your first name: ").upper()
sLastName = input("Enter your last name: ").upper()
sAddress = input("Enter your street address: ")
sCity = input("Enter your city: ")
sState = input("Enter your state: ").upper()
sBirthYear = input("Enter your birth year: ")

#Calculate age
iAge = 2021 - int(sBirthYear)

#Print concatenated full name
print(sFirstName, sLastName)
#Print address
print(sAddress)
#Print city and state separated by a tab
print(sCity,sState, sep="\t")
#Print age and
print("In 2021",sFirstName,"was",iAge,"years old.")