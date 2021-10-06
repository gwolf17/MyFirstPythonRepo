"""
Gillian Wolfersberger
This is a program to practice finding errors and creating exceptions in a program.
"""

try:
    #import MyLibrary

    iCount = 245
    iNumTests = 0

    sName = "Alfalfa"

    #fAve = iCount/iNumTests  
    #print(fAve)
    #print(sName[15])
    #fNewFile = open("test")
except ImportError:
    print("Cannot import file.")
except ZeroDivisionError:
    print("Divide by zero error.")
except NameError:
    print("Variable is not defined.")
except IndexError:
    print("String index is out of range.")
except FileNotFoundError:
    print("File not found.")
except Exception as eError:
    print(eError)