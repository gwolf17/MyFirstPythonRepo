"""
Gillian Wolfersberger
This program creates a customer class and allows the user to create a new customer based on keyboard inputs
"""

#Create customer class
class Customer:
    #Common class variable
    companyName = "ABC Accounting"
    
    #Constructor and creation of instance variables based on data input from the customer
    def __init__ (self, custID, custName, account, balance):
        self.customer_ID = custID
        self.customer_name = custName
        self.account = account
        self.balance = balance

    #Method to display customer information
    def display_customer (self):
        print(self.customer_name, " has a balance of $", self.balance, sep="")

#Create variables from customer inputs
icustID = int(input("Enter Customer ID: "))
scustName = input("Enter Customer Name: ").title()
iaccount = int(input("Enter Account Number: "))
fbalance = float(input("Enter Account Balance: "))

#Create a new customer
cust1 = Customer(icustID, scustName, iaccount, fbalance)

#Print customer information through calling the display_customer method
cust1.display_customer()