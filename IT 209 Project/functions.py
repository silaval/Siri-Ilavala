#Import statements:
import random

#------------------------------------------------------------------------------------------
def firstname(f):
    '''This function extracts the first name from the user input '''
    name = f.split(' ') # Temporary variable to obtain first name
    firstname = name[0] # First name used to greet user
    firstname = firstname.title()
    return firstname

#------------------------------------------------------------------------------------------
def confirmation(person, sv):
    """This function has the user confirm their personal information. """
    print("\nPlease confirm the following information:\n")
    count = 1
    for info in person:
        print("[",count,"] - ",info)
        count += 1
    print()
    confirm = input('Is your information listed above correct ("yes" or "no"): ')
    confirm = confirm.lower()
    while (confirm != 'yes') and (confirm != 'no'):
        print("ERROR! Invalid Input")
        confirm = input('\nPlease confirm the updated information above, type "yes" or "no": ')
        confirm = confirm.lower()
    while confirm == 'no':
        correction = int(input('\nWhat information would you like to correct? Type the ' +\
                               'option number that is listed to the left of each line: '))
        correction -= 1
        correction_info = input('\nPlease type the correct ' + sv[correction] +\
                                ': ')
        if correction == 4:
            correction_info = correction_info.upper()
        else:
            correction_info = correction_info.title()
        person[correction] = correction_info
        print()
        # Confirm user's updated information:
        print('Please confirm the updated information:\n')
        count = 1
        for info in person:
            print('[',count,'] - ',info)
            count += 1
        print()
        confirm = input('Is the updated information above correct ("yes" or "no"): ')
        confirm = confirm.lower()
        while (confirm != 'yes') and (confirm != 'no'):
            print("ERROR! Invalid Input")
            confirm = input('Please confirm the updated information above, type "yes" or "no": ')
            confirm = confirm.lower()
    # If the information is correct, the list of information is returned:
    return person

#---------------------------------------------------------------------------------------------

def username():
    '''This function allows the user to create their username'''
    print("GMU banking creates usernames for its users in a standard format.")
    print("The format is firstLetterOfFirstName.LastName(A Randomly Generated Number).")
    print("\nPlease enter the following information to create you username: \n")
    letter = input("Please enter the first letter of your first name: ")
    letter = letter.lower()
    
    lastName = input("Please enter your last name: ")
    lastName = lastName.lower()
    
    num = random.randint(0, 9)

    un = (letter + "." + lastName + str(num))

    return un

#---------------------------------------------------------------------------------------------

def password():
    '''This function allows the user to create a password for their account'''
    print("\nGMU banking creates passwords by having you the user enter in a password of your choice, then select " +\
          "three random letter and adds it to the beggining of your password, and then randomly generate three numbers " +\
          "and attaches those 3 number to the end of your password to create a well encrypted password.")

    print("\nSo lets get started\n")

    password = input("Please enter the password you wish to keep for your account. It must be more than 8 characters: ")
    
    while True:
        if len(password) >= 8:
            print("\nPassword Approved!\n")
            break
        else:
            print("-ERROR! Invalid Password! - Password must be 8 characters or more!!!-")
            password = input("Please enter another password for your account: ")

    letters = input("Please enter 3 random letters: ")
    while True:
        if len(letters) != 3:
            print("-ERROR! Only three letters allowed!-")
            letters = input("Please enter 3 random letters: ")
        break
    nums = random.randint(100, 999)

    npw = letters + password + str(nums)
    
    return npw

#---------------------------------------------------------------------------------------------

def pin():
    '''This function allows the user to create a pin for their account'''
    
    p = input("\nPlease choose a 4 digit pin for your account: ")
    
    while True:
        if len(p) == 4:
            if p.isdigit():
                break
            else:
                print("-ERROR! Invalid Pin! - PIN MUST BE NUMBERS ONLY-")
                p = input("Please enter a different pin for you account: ")
        else:
            print("-ERROR! Invalid Pin! - PIN MUST BE 4 DIGITS AND NUMBERS ONLY!!!-")
            p = input("Please enter a different pin for you account: ")

    pinNum = p

    return pinNum

#---------------------------------------------------------------------------------------------

def securityQuestions():
    '''This function shows user three security questions to answer and saves to answers'''

    #defines file name
    fileName = "securityQuestions.txt"

    #creates an empty list
    sqQuestions = []
    answers = []
    qa = {}

    #opens file to read
    file = open(fileName, "r")

    #Starts a counter
    lineNum = 1

    print("|-----------------------------------------------------------------------------|")
    #loops through file adding each line to the list
    for i in file:
        sqQuestions.append(i.strip())
        print("\n  ", lineNum, ":", i)
        if lineNum != 5:
            print("|-----------------------------------------------------------------------------|")
        lineNum += 1
    print("\n|-----------------------------------------------------------------------------|")
    
    question1 = int(input("\nPlease pick one line number to the left of a question you wish to answer: "))
    while True:
        if (question1 > 5) or (question1 <= 0):
            print("\n-ERROR! Input must be 1, 2, 3, 4, or 5-")
            question1 = int(input("Please pick one line number to the left of each question, above, to answer: "))
        else:
            break
    q1 = question1-1
    print("\nFirst questions selected -- \"" + sqQuestions[q1] + "\"")
    answer1 = input("\nPlease type your answer to this questions: ")

    question2 = int(input("\n-\n\nPlease pick another line number to the left of a question to answer: "))
    while True:
        if (question2 > 5) or (question2 <= 0):
            print("\n-ERROR! Input must be 1, 2, 3, 4, or 5-")
            question2 = int(input("Please pick another line number to the left of each question, above, to answer: "))
        if(question2 == question1):
            print("\n-ERROR! This question was already chosen!!!-")
            question2 = int(input("Please pick another line number to the left of each question, above, to answer: "))
        else:
            break
    q2 = question2-1
    print("\nSecond questions selected -- \"" + sqQuestions[q2] + "\"")
    answer2 = input("\nPlease type your answer to this questions: ")

    question3 = int(input("\n-\n\nPlease pick one more line number to the left of a question to answer: "))
    while True:
        if (question3 > 5) or (question3 <= 0):
            print("\n-ERROR! Input must be 1, 2, 3, 4, or 5-")
            question3 = int(input("Please pick one more line number to the left of each question, above, to answer: "))
        if(question3 == question1) or (question3 == question2):
            print("\n-ERROR! This question was already chosen!!!-")
            question3 = int(input("Please pick one more line number to the left of each question, above, to answer: "))
        else:
            break
    q3 = question3-1
    print("\nThird questions selected -- \"" + sqQuestions[q3] + "\"")
    answer3 = input("\nPlease type your answer to this questions: ")

    qa.update({sqQuestions[q1] : answer1})
    qa.update({sqQuestions[q2] : answer2})
    qa.update({sqQuestions[q3] : answer3})

    print("\n\nThe Security questions and theirs answers (PLEASE TAKE NOTE OF THEM):\n")

    count = 1
    for k, v in qa.items():
        print (count, ":",k, " -- ", v)
        count += 1

    return "    " + sqQuestions[0] + " -- " + answer1 + "\n" + "    " + sqQuestions[1] + " -- " + answer2 + "\n" + "    " + sqQuestions[2] + " -- " + answer3



#---------------------------------------------------------------------------------------------

def balance(value):
    balance = 0
    newBalance = balance + value
    return newBalance

