#------------------------------------------------------------------------------
# IT 109 Project
# Siri Ilavala
# G01136962
# IT 109 Section 001
# Ponkas Das
# Nov. 26, 2019
#------------------------------------------------------------------------------

#Import Statements:
import functions
import random

#Variables:
username = " "
password = " "

#User information constants:
NAME = 'Name '
TELNUM = 'Telephone Number '
ADDRESS = 'Street Address '
CITY = 'City '
STATE = 'State (Abbr.) '
ZIP = 'Zip Code '
DOB = 'Date of Birth '
SSN = 'Social Security Number '
newUser_info = []
newUser_info.extend((NAME, TELNUM, ADDRESS, CITY, STATE, ZIP, DOB, SSN))

# User:
user_telnum = ''
user_address = ''
user_city = ''
user_state = ''
user_zip = ''
user_dob = ''
user_ssn = ''
user_info = []


#______________________________________________________________________________
#-Greets user-------------------------------------------------------------------

print("Hello. Welcome to GMU Bank account creator service!")

user_name = input("Please enter your full name: ")

user_firstName = functions.firstname(user_name)

user_info.append(user_name)

print("Hi",user_firstName)

create_account = input("Do you wish to create a GMU bank account right now? (\"yes\" or \"no\"): ")

create_account = create_account.lower()

while (create_account != "yes") and (create_account != "no"):
    print("Invalid response. Please try again")
    create_account = input("Do you wish to create a GMU bank account right now? (\"yes\" or \"no\"): ")
    create_account = create_account.lower()

#_________________________________________________________________________________
#-Collects user's information if user wishes to create an account-------------------


if create_account == "yes":
    print("\nGreat! Let's get started.")

    account_num = random.randint(100, 300)
    print("\nYour randomly generated account number is", account_num)
    print("\nPLEASE TAKE NOTE OF YOUR ACCOUNT NUMBER ABOVE!")

    print("\nPlease input the following information below:")
    print("----------------------------------------------------------------------------")
    user_telnum = input(newUser_info[1] + "(Please enter without spaces or dashes) : ")
    t = user_telnum.isdigit()
    while (t == False) or (len(user_telnum) != 10):
        print("Error! Please follow format and try again!!!")
        user_telnum = input(newUser_info[1] + "(Please enter without spaces or dashes) : ")
        t = user_telnum.isdigit()

    user_address = input(newUser_info[2] + ": ").title()
    user_city = input(newUser_info[3] + ": ").title()
    user_state = input(newUser_info[4] + ": ").upper()
    user_zip = input(newUser_info[5] + ": ")
    user_dob = input(newUser_info[6] + "(Please enter in mmddyyyy format) : ")
    d = user_dob.isdigit()
    while (d == False) or (len(user_dob) != 8):
        print("Error! Please follow format and try again!!!")
        user_dob = input(newUser_info[6] + "(Please enter in mmddyyyy format) : ")
        d = user_dob.isdigit()
    
    user_ssn = input(newUser_info[7] + "(Please enter without spaces or dashes) : ")
    s = user_ssn.isdigit()
    while (s == False) or (len(user_ssn) != 10):
        print("Error! Please follow format try again!!!")
        user_ssn = input(newUser_info[7] + "(Please enter without spaces or dashes) : ")
        s = user_ssn.isdigit()

    user_info.extend((user_telnum, user_address, user_city, user_state, user_zip, user_dob, user_ssn))

    # Cofirmation of information from user's input:
    user_info = (functions.confirmation(user_info, newUser_info))


#__________________________________________________________________________________________________
#_Creates user's username, password, and security pin-------------------------------------------------------------

    print("\n\nAlright, now lets move on create your username, password, and pin.")
    print("\nPLEASE READ ALL OF THE FOLLOWING CAREFULLY")
    print("\n----------------------First, we will create your username.----------------------\n")

    username = functions.username()

    print("\nYour username is", username)

    print("\n--------------------------Now lets create your password.-------------------------")
    password = functions.password()
    print("\nYour encrypted password is", password)


    print("\n-------------------------Next, lets create your pin.------------------------")
    pin = functions.pin()
    print("\nYour pin number is", pin)
    
    
    print("\n\nPlease take note of your username, password, and pin!!!")
    
    print("\nHere is your username, password, and pin once again.\n")
    
    print("\t|--------------------------------|")
    print("\t  Username:", username)
    print("\t|--------------------------------|")
    print("\t  Password:", password)
    print("\t|--------------------------------|")
    print("\t  Pin:", pin)
    print("\t|--------------------------------|")

    print("\nPLEASE TAKE NOTE OF THEM!!!")

    print("\nYou have just finished setting up your Username, Password, and Pin!")

#__________________________________________________________________________________________________
#_Allows user to pick answers for security questions-----------------------------------------------

    print("\n\nNext, we will have to choose three security questions for your account and their answers.\n")
    print("Security Questions:\n")
    secQue = functions.securityQuestions()

    print("\nYou have just finished picking security questions and setting their answers!")

    print("\nWe are just about done with setting up your account!")

    print("\nPlease take note of the following information about your account:\n")

    print("|---------------------------------------------------------------------------------|")
    print("  Account Number:", account_num)
    print("|---------------------------------------------------------------------------------|")
    print("  Username:", username)
    print("|---------------------------------------------------------------------------------|")
    print("  Password:", password)
    print("|---------------------------------------------------------------------------------|")
    print("  Pin Number:", pin)
    print("|---------------------------------------------------------------------------------|")
    print("  Security Questions and their answers:")
    print(secQue)
    print("|---------------------------------------------------------------------------------|")

    print("\n\nPLEASE TAKE NOTE OF THE ABOVE INFROMATION!!!!\n\n")

    print("|-----------------------------------------------------------------|")
    print("|  CONGRATS! You have successfully created a GMU BANK account!!!  |")
    print("|-----------------------------------------------------------------|")

    deposit = input("\n\nYour current balance is $0, would you like to transfer money into your account? (\"yes\" or \"no\"): ")
    deposit = deposit.lower()
    
    while (deposit != "yes") and (deposit != "no"):
        print("Invalid response. Please try again")
        deposit = input("Your current balance is $0, would you like to transfer money into your account?  (\"yes\" or \"no\"): ")
        deposit = deposit.lower()

    if (deposit == "yes"):
        transAccount = input("Please enter the account number from which you will transfer the money: ")
        transBank = input("Please enter the bank name from where you will transfer the money: ")
        amount = float(input("Please enter the amount you wish to transfer to your account : "))
        currentBalance = functions.balance(amount)
        print("Your new balance is $" + str(currentBalance))
        print("\nTHANK YOU FOR USING GMU BANKING, HAVE A NICE DAY!!!")
    elif (deposit == "no"):
        print("\nTHANK YOU FOR USING GMU BANKING, HAVE A NICE DAY!!!")


else:
    print("\nThank you for visiting GMU Bank account services, have a nice day!")




