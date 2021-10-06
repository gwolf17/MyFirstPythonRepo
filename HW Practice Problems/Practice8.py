"""
Gillian Wolfersberger
This program uses user input and a function to calculate weekly take home pay
"""
#Import the calc_pay function from the wage_functions file
from wage_function import calc_pay

#Gather inputs from user and assign them to variables
sName = input("Please enter your name: ").title()
iHours = int(input("How many hours did you work this week?: "))
fWage = float(input("What is your hourly wage?: "))
fTax = float(input("What is the tax rate (i.e. 3.2)?: "))
fFICA = float(input("What is the FICA rate (i.e. 7.65)?: "))

#Call the cal_pay function from the wage_functions file
fTakeHome = calc_pay(iHours, fWage, fTax, fFICA)

#Print results
print(sName, " worked ", iHours, " hours in the week at $", fWage, " an hour and took home $", fTakeHome, ".", sep="")
