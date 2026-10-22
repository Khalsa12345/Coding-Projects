import random


def checkLen():
    password = input("\nPlease enter a password: ")
    passlen = len(password)
    if 8< passlen <25:
        return True, passlen, password    
    else:
        print("Invalid Password. Returning to menu...")
        return False, 0, ""

def checkPass(passlen, password):
    allowedCh = open("AllCh.txt" , "r")
    score = passlen
    listCh = []
    upperCh = []
    count = 0
    onlyLetters = True
    onlyDigit = True
    for line in allowedCh:
        listCh.append([line.strip()])
    for i in range(0,4):
        for letter in password:
            if letter in listCh[i][0]:
                score += 5
                count += 1
                break
    if count == 4:
        score += 10
    for letter in password:
        if letter not in listCh[0][0] and letter not in listCh[1][0]:
            onlyLetters = False
            break
    for letter in password:
        if letter not in listCh[2][0]:
            onlyDigit = False
            break
    if onlyLetters == True:
        score -= 5
    if onlyDigit == True:
        score -= 5
    allowedCh.close()
    upperFile = open("UpperCharacters.txt" , "r")
    for line in upperFile:
        upperCh.append(line.strip())
    for i in range(0, passlen - 2):
        chunk = password[i:i+3].lower()
        for row in upperCh:
            if chunk in row:
                score -= 5
    if score > 20:
        print(f"""\n\tPassword: {password}
\tScore: {score}
\tStrength: Strong""")
    elif score > 0 and score < 20:
        print(f"""\n\tPassword: {password}
\tScore: {score}
\tStrength: Medium""")
    elif score < 0:
        print(f"""\n\tPassword: {password}
\tScore: {score}
\tStrength: Weak""")
    print("\n*************************************************")
    upperFile.close()
    return listCh, upperCh


def genPass():
    listChG = []
    allowedCh = open("AllCh.txt" , "r")
    for line in allowedCh:
        listChG.append(line.strip())
    Gpasslen = random.randint(8,12)
    randomPass = ""
    for i in range(Gpasslen + 1):
        randomRow = random.choice(listChG)
        randomLetter = random.choice(randomRow)
        randomPass += randomLetter
    print("Generating Password...")
    print(f"Generated Password: {randomPass}")
    checkPass(Gpasslen, randomPass)
    allowedCh.close()
    



def menu():
    print("Welcome to the password checker.")
    
    while True:
        print("""\n\tMain Menu

\t1. Check Password

\t2. Generate Password

\t3. Quit""")
        try:
            option = int(input("\nPlease choose an option below: "))
            if option == 1:
                valid, passlen, password = checkLen()
                if valid == True:
                    checkPass(passlen, password)        
            elif option == 2:
                genPass()
            elif option == 3:
                print("Thank you for using the password checker. Press Enter to exit.")
                quit()
            else:
                print("Inavlid option! Please choose from 1-3: ")
        except ValueError:
            print("Enter a number!")
    
menu()
