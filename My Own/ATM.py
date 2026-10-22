balance = int(input("Please enter your bank balance: "))
pin = 1234
count = 0

def balanceM(balance):
    print(balance)

def withdraw(balance):
    withdrawA = int(input("How much do you want to withdraw? "))
    if withdrawA > balance:
        print("Insufficient Funds.")
    else:
        newTotal = balance - withdrawA
        print(f"Your new balance is {newTotal}")
        balance = newTotal
    return balance
        
def menu(balance):
    while True:
        print("""\n\t\t1. Check Balance
        \t2. Withdraw money
        \t3. Exit""")
        try:
            option = int(input("\nPlease choose an option from 1-3: "))
            if option == 1:
                balanceM(balance)
            elif option == 2:
                balance = withdraw(balance)
            elif option == 3:
                print("Thank you for using the ATM. Press enter to exit.")
                quit()
        except ValueError:
            print("Enter a number!")

while True:
    attempt = int(input("Please enter your pin: "))
    count += 1
    if attempt == pin:
        print("Pin Valid")
        menu(balance)
        break
    else:
        print("Invalid Pin")
        if count >= 3:
            print("Card Blocked")
            break

