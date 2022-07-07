import re
import os
import fileinput


def createTxt():
    database = 'db.txt'
    if os.path.exists(database):
        pass
    else:
        with open('db.txt', 'w') as f:
            f.write('username,password')

def passValidLenght(password):
    if 6 <= len(password) <= 15:
        return True
    else:
        return False

def userValidLength(username):
    if 3 <= len(username) <= 15:
        return True
    else:
        return False

def containDigits(password):
    a = 0
    for i in password:
        if i.isdigit():
            a+=1
    if a > 0:
        a = 0
        return True
    else:
        return False

def containAlpha(password):
    a = 0
    for i in password:
        if i.isalpha():
            a+=1
    if a > 0:
        a = 0
        return True
    else:
        return False

def containSpaces(password):
    a = 0
    for i in password:
        if i.isspace():
            a+=1
    if a > 0:
        a = 0
        return True
    else:
        return False

def containSpecialCharacters(password):
    a = 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(password) == None:
            a+=1
    if a > 0:
        a = 0
        return True
    else:
        return False

def containCapital(password):
    a = 0
    for i in password:
        if i.isupper():
            a+=1
    if a > 0:
        a = 0
        return True
    else:
        return False

def passwordConfirmation(password):
    confPassword = input("Confirm your password : ")
    if confPassword == password:
        return True
    else:
        return False

def notTheSameUserPass(username,password):
    if username == password:
        return True
    else:
        return False

def passwordValidations(username, password):
    errorsp = []
    if not passValidLenght(password):
        errorsp.append("Please type in password between 6 and 15 characters.")
    if not containDigits(password):
        errorsp.append("Please type in password that contains digits.")
    if not containAlpha(password):
        errorsp.append("Please type in password that contains at least one alphabetical character.")
    if containSpaces(password):
        errorsp.append("Please type in password that doesn't contain spaces.")
    if containSpecialCharacters(password):
        errorsp.append("Please type in password that contains at least one special character.")
    if not containCapital(password):
        errorsp.append("Please type in password that contains at least one capital letter.")
    if notTheSameUserPass(username, password):
        errorsp.append("Username and password cannot be the same.")
    if not passwordConfirmation(password):
        errorsp.append("Passwords doesn't match.")
    if errorsp != []:
        for i in errorsp:
            print(i)
        errorsp = []
        return False
    else:
        errorsp = []
        return True
        
def usernameExists(username):
    with open("db.txt", "r") as f:
        a = 0
        for line in f:
            db = list(line.split(","))
            if username == db[0]:
                a+=1
        if a > 0:
            a = 0
            return True
        else:
            return False

def userExistCheck(username):
    if usernameExists(username) is True:
        print("Username aleady exists.")
    else:
        pass

def usernameVerification(username):
    errorsu = []
    if usernameExists(username):
        errorsu.append("Username aleady exists.")
    if not userValidLength(username):
        errorsu.append("Please type in username between 3 and 15 characters.")
    if errorsu != []:
        for i in errorsu:
            print(i)
        errorsu= []
    else:
        errorsu = []
        return False

def addCredentials(username, password):
    with open("db.txt", "a") as f:
        f.write("\n" + username + "," + password)

def passCheck(username, password):
    with open("db.txt", "r") as f:
        a = 0
        for line in f:
            credentials = (username + "," + password)
            if credentials == line:
                a+=1
        if a > 0:
            a = 0
            return True
        else:
            return False

def Register():
    user = input("Please type in your username: ")
    while usernameVerification(user) is False:
        userExistCheck(user)
        _pass = input("Please type in password: ")
        while passwordValidations(user, _pass) is False:
            _pass = input("Please type in password: ")
        if passwordValidations(user, _pass) is True:
            addCredentials(user, _pass)
            print("Success!")
        else:
            pass
        break    

def loginHandler(username, password):
    if passCheck(username, password) is True:
        print("You have been successfully logged in.")
        return True
    else:
        print("Incorrect password. Please try again.")

def passwordChange(username,password):
    f = open("db.txt")
    oldPassw = input("Please enter your password: ")
    if oldPassw == password:
        newPassw = input("Please type in new password: ")
        while passwordValidations(username,newPassw) is True:
            #newPasswConf = input("Please onfirm new password: ")
            #if newPassw == newPasswConf:
            #for i in fileinput.input(f, inplace = 1):
            for i in f:
                if i == (username + "," + password):
                    i.replace(password, newPassw)
                    f.close
            else:
                break
            



def Login():
    user = input("Please type in your username: ")
    if usernameExists(user) is False:
        print("Incorrect username. Please try again.")
    while usernameExists(user) is True:
        _pass = input("Please type in password: ")
        if loginHandler(user, _pass) is True:
            passChangeConfirmation = input("Would you like to change your password? ")
            answers = ['yes', 'yup', 'yaaas', 'yaas', 'ofc', 'tak']
            if passChangeConfirmation.lower() in answers:
                passwordChange(user,_pass)
            else:
                break

def mainLoop():
    action = input("Type 1 if you want to login, type 2 if you want to register: ")
    try:
        if action == "1":
                Login()
        elif action == "2":
            Register()
        else:
            print("It's not 1 or 2")
    except:
        if action == "quit":
            quit

while True:
    createTxt()
    mainLoop()
