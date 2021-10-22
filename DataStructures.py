"""
Authors:

Gillian Wolfersberger
Tyler Herd
Jacob Long
Royce Cotcher

Program Description: 

Create a queue of orders, keep track of how many burgers each customer orders,
and output the total amount of burgers that each customer ordered
"""

import random

#VARIABLES
#Create an empty dictionary to hold customer information
dictCustomerInfo = {}
#Create list variable to hold sorted dictionary values
listSortedCustomers = []
#Create an empty list to represent the line of customers
lstQueue = []

class Order :
    #Constructor
    def __init__ (self):
        #Populate instance variable by calling randomBurgers function
        self.burger_count = self.randomBurgers()

    #Function that creates a random #
    def randomBurgers(self):
         return random.randint(1, 20)

class Person :
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]

    def __init__(self):
        #Assign a random name by calling the randomName function
        self.customer_name = self.randomName()
        

    #Function that returns a random name from a list of 9 customers
    def randomName(self):
        
        return random.choice(self.asCustomers)

#Customer class inherits from Person class
class Customer (Person):
    #Constructor
    def __init__ (self):
        #Call parent constructor
        super().__init__()
        #Create a new Order object and assign it to the order instance variable
        self.order = Order()

#Fill the listQueue list with 100 Customer objects
for iCount in range(0, 100):
    lstQueue.append(Customer())

#Process queue and record total amount of burgers ordered by each person
for iCount in range(0, len(lstQueue)): 
    #Determine if the customer has been added to the dictionary yet or not
    if lstQueue[iCount].customer_name in dictCustomerInfo:
        #If customer is in the dictionary, add burger count to value
        dictCustomerInfo[lstQueue[iCount].customer_name] += lstQueue[iCount].order.burger_count
    else:
        #If customer is not in the dictionary, add the customer as the key and the burger count as the value
        dictCustomerInfo[lstQueue[iCount].customer_name] = lstQueue[iCount].order.burger_count


#Sort the values of the dictionary in descending order and assign to list variable
listSortedCustomers = sorted(dictCustomerInfo.items(), key=lambda x: x[1], reverse=True) 

#For loop to check if a customer never ordered any burgers
for iCount in range(0,len(dictCustomerInfo)):
    #See if current person ordered burgers, if not, output 0 burgers ordered
    if Person.asCustomers[iCount] in dictCustomerInfo:
        pass
    else:
        #Add customer name to list
        listSortedCustomers.append((Person.asCustomers[iCount], '0 <- Poor guy'))

#For loop to output each element of the sorted customers list
for iCount in range(0, len(listSortedCustomers)): 
    sOutput = str(listSortedCustomers[iCount][0].ljust(19)) + '\t\t' + str(listSortedCustomers[iCount][1])
    print(sOutput)