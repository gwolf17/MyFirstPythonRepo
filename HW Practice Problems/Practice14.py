"""
Gillian Wolfersberger
THis program demonstrates the efficiency of using the list, set, and dictionary for adding items, searching for an item, and deleting items
"""

#Import date time module
import datetime

#ADD ITEMS
#Create empty list variable
lstList = []
#Save start time
startTime = datetime.datetime.now()
for iCount in range(0, 500000):
    lstList.append('Customer' + str(iCount))
#Save end time
endTime = datetime.datetime.now()
#Compute total time to populate list
totalTime = (endTime - startTime).microseconds
#Print results
print("List add: " + str(totalTime) + "\n")

#Create empty set
stSet = set()
#Save start time
startTime = datetime.datetime.now()
for iCount in range(0, 500000):
    stSet.add('Customer' + str(iCount))
#Save end time
endTime = datetime.datetime.now()
#Compute total time to populate set
totalTime = (endTime - startTime).microseconds
#Print results
print("Set add: " + str(totalTime) + "\n")

#Create empty dictionary
dictDictionary = {}
#Save start time
startTime = datetime.datetime.now()
for iCount in range(0, 500000):
    dictDictionary[iCount] = 'Customer' + str(iCount)
#Save end time
endTime = datetime.datetime.now()
#Compute total time to populate dictionary
totalTime = (endTime - startTime).microseconds
#Print results
print("Dictionary add: " + str(totalTime) + "\n\n")


#SEARCH FOR MIDDLE VALUE
#List
#Save start time
startTime = datetime.datetime.now()
#Find Customer250000 in list
if "Customer250000" in lstList:
    #Save end time
    endTime = datetime.datetime.now()
    #Compute total time to find Customer250000
    totalTime = (endTime - startTime).microseconds
    #Print results
    print("List find: " + str(totalTime) + "\n")

#Set
#Save start time
startTime = datetime.datetime.now()
#Find Customer250000 in Set
for sValue in stSet:
    if sValue == "Customer250000":
        #Save end time
        endTime = datetime.datetime.now()
        #Compute total time to find Customer250000
        totalTime = (endTime - startTime).microseconds
        #Print results
        print("Set find: " + str(totalTime) + "\n")

#Dictionary
#Save start time
startTime = datetime.datetime.now()
#Fid Customer250000 in Dictionary
if 250000 in dictDictionary:
    #Save end time
    endTime = datetime.datetime.now()
    #Compute total time to find Customer250000
    totalTime = (endTime - startTime).microseconds
    #Print time
    print("Dictionary find: " + str(totalTime) + "\n\n")


#DELETE VALUES ONE AT A TIME
#List
#Save start time
startTime = datetime.datetime.now()
#Delete all items from List one at a time
for iCount in range(0, len(lstList)):
    lstList.pop(0)
#Save end time
endTime = datetime.datetime.now()
#Compute total time to delete all items
totalTime = (endTime - startTime).microseconds
#Print results
print("List delete element: " + str(totalTime) + "\n")

#Set
#Save start time
startTime = datetime.datetime.now()
#Delete all items from Set one at a time
for iCount in range(0, len(stSet)):
    stSet.pop()
#Save end time
endTime = datetime.datetime.now()
#Compute total time to delete all items
totalTime = (endTime - startTime).microseconds
#Print results
print("Set delete element: " + str(totalTime) + "\n")

#Dictionary
#Save start time
startTime = datetime.datetime.now()
#Delete all items from Dictionary one at a time
for iCount in range(0, len(dictDictionary)):
    dictDictionary.pop(iCount)
#Save end time
endTime = datetime.datetime.now()
#Compute total time to delete all items
totalTime = (endTime - startTime).microseconds
#Print results
print("Dictionary delete element: " + str(totalTime))