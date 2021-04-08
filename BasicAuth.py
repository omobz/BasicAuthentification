import datetime
now = datetime.datetime.now()
print('current date and time : ')
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#register
# -FirstName, Last name password, email
#generate account number

#login
# -Account Number and password

#bank operations

#initializing the system

import random

database = {} #dictionary

def init(): 
    
    print("Welcome to Zee bank")
    
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n "))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('Invalid Option Exit or Try Again')
        init()


    
def login():
    print("********* Login ***********")
    accountNumberFromUser = int(input("Enter Account Number \n"))
    password = input("Enter Password \n")
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                    bankOperation(userDetails)

    print('invalid account or password')
    login()


def register():

    print('***** REGISTER *****')
    email = input('Enter your email address \n')
    firstName = input(' Enter First name \n')
    lastName = input(' Enter Last name \n')
    password = input('create your password \n')

    accountNumber = generateAccountNumber()
    
    database[accountNumber] = [ firstName, lastName, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Thank you for choosing Zee Bank")
    print(" == ==== ====== ===== ===")
    
    login()
    
def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    
    
    selectedOption = int(input("What would you like to do: 1 Deposit 2 Withdraw 3 logout \n"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation
    elif (selectedOption == 3):
        exit()
    else:

        print('invalid option selected')
        bankOperation(user)

def withdrawalOperation():
    print('withdrawal')

def depositOperation():
    print('deposits')

def exit():
    print('EXIT')

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

init()