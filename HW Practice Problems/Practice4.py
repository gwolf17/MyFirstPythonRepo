"""
Gillian Wolfersberger
This is a program that generates test score averages for two individuals and then compares them to each other"""

#Promt inputs for first individual
sFirstFullName = input("What is the first person's full name?: ").upper()
iFirstBirthYear = input("What is the first person's birth year?: ")
iFirstSum = int(input("What is the sum of all test scores for the first pereson?: "))
iFirstTests = int(input("How many tests did the first person take?: "))

#Prompt inputs for the second individual
sSecondFullName = input("What is the second person's full name?: ").upper()
iSecondBirthYear = input("What is the second person's birth year?: ")
iSecondSum = int(input("What is the sum of all test scores for the second pereson?: "))
iSecondTests = int(input("How many tests did the second person take?: "))

#Calculate averages
fFirstAvg = round((iFirstSum/iFirstTests), 1)
fSecondAvg = round((iSecondSum/iSecondTests), 1)

#Print results
print(sFirstFullName,"born in",iFirstBirthYear,"scored",iFirstSum,"points on",iFirstTests,"for an average of",fFirstAvg,"%.")
print(sSecondFullName,"born in",iSecondBirthYear,"scored",iSecondSum,"points on",iSecondTests,"for an average of",fSecondAvg,"%.")
print("Did ",sFirstFullName," score higher than ",sSecondFullName,"?", sep="")

#Determine if person one had a higher average than person two
print(fFirstAvg>fSecondAvg)