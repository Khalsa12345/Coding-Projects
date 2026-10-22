import random
import time


def genKey():
    key = ""
    keyCode = ""
    sumCode = 0
    for j in range(0,8):
        num1 = random.randint(33,126)
        letter1 = chr(num1)
        key += letter1
    print(f"""
**********************************************************
    
    \tCharacter Key: {key}

**********************************************************""")
    for i in key:
        code1 = ord(i)
        sumCode += code1
        keyCode += str(code1)

    offset = (sumCode // 8) - 32
        
        
    return key, offset



def openFile():
    option = input("Please enter the name of the file: ")
    if ".txt" not in option:
        option += ".txt"
    try:
        file = open(option, "r")
        text = file.read()
        file.close()
    except FileNotFoundError:
        print("File does not exist.")
        print("Returning to menu...")
        return None
    return text

def encrypt():
    asciiNum = 0
    encLetter = ""
    encSentence = ""
    text = openFile()
    if text is None:
        return 
    key, offset = genKey()
    for letter in text:
        if letter != " ":
            asciiNum = ord(letter)
            num = asciiNum + offset
            if num > 126:
                num -= 94
            encLetter = chr(num)
            encSentence += encLetter
        else:
            encSentence += " "
    print("Encrypting File...")
    time.sleep(2)
    print("File Encrypted!")
    print(encSentence)
    filename = input("What would you like to call your file? ")
    if ".txt" not in filename:
        filename += ".txt"
    file = open(filename, "w")
    file.write(encSentence)
    file.close()
    return key, offset, encSentence





def menu():
    print("Welcome to the encrypter")
    while True:
        try:
            print("""\n\t\t1. Encrypt Message
\t\t2. Decrypt Message
\t\t3. Exit""")
            option = int(input("\nPlease choose an option from 1-3: "))
            if option == 1:
                result = encrypt()
                if result is not None:
                    key, offset, encSentence = result
            elif option == 2:
                print("TEMP2")
            elif option == 3:
                print("Thank you for using the encrypter. Press enter to exit.")
                quit()
        except ValueError:
            print("Choose a number!")
menu()
                
                
