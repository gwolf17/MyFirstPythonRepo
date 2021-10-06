"""
Gillian Wolfersberger
This program allows a user to enter data for a customer through the use of classes
"""

#Person class (owner of customer class)
class Person():
        def __init__(self, name, address, city, state, zip):
            self.name = name
            self.address = address
            self.city = city
            self.state = state
            self.zip = zip

#Customer class (inherits from person class)
class Customer(Person):

    #Class variable
    our_company = "ABC Accounting"

    #Constructor
    def __init__ (self, name, address, city, state, zip, num_employees):
        #Call super and pass instance variable to person constructor
        super().__init__(name, address, city, state, zip)

        #Assign num_employees instance variable
        self.num_employees = num_employees

        #Create account by calling account class
        self.account = Account()

        #Call gen_account method from Account class
        self.account.gen_account(self.name, self.address)
 
    #print_customer method
    def print_customer(self):
        print(self.name + " with account " + self.account.account_number + " owes $" + str(self.account.balance) + ".")

#Account class
class Account():

    #Empty constructor
    def __init__ (self):
        pass

    #set_balane method
    def set_balance(self, balance):
        self.balance = balance

    #gen_account method
    def gen_account(self, name, address):
        #Create instance variable that takes the first 3 characters from the name and address variables and puts them together
        self.account_number = name[0:3] + address[0:3]


#Gather user inputs and assign to variables
sName = input("Enter customer name: ").title()
sAddress = input("Enter street address: ")
sCity = input("Enter city: ").title()
sState = input("Enter state: ").upper()
sZip = input("Enter zip code: ")
fBalance = float(input("Enter account balance: "))
iNumEmployees = int(input("Enter the number of employees: "))

#Create a new customer object
oCustomer = Customer(sName, sAddress, sCity, sState, sZip, iNumEmployees)
#Call set_balance method to set the account balance
oCustomer.account.set_balance(fBalance)
#Display customer information through calling the print_customer method
oCustomer.print_customer()