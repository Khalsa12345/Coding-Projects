import random


def cards():
    dogs = {}
    dogNames = open("dogs.txt", "r")
    for line in dogNames:
        keyName = line.strip().lower()
        dogs[keyName] = {
                         "exercise" : random.randint(1,5),
                         "intelligence" : random.randint(1,100),
                         "friendliness" : random.randint(1,10),
                         "drool" : random.randint(1,10)} # A nested dictionary. Currently, it's massive but its fine as only the main info can be retrieved.
    dogNames.close()
    return dogs
    


def play():
    try:
        print("\nChoose an even number greater than 4 and less than 30")
        numOfCards = int(input("Please enter the number of cards to be played: "))
        if not (4< numOfCards <30) or numOfCards %2 != 0:
            print("\nChoose an even number and greater than 4 but less than 30!")
            print("Returning to menu...")
            return
    except ValueError:
        print("Choose a number! Returning to menu...")
        return
    dogs = cards()
    lengthDogs = len(dogs)
    shuffledCards = random.sample(list(dogs.items()), numOfCards)
    halfway = numOfCards // 2
    playerCards = shuffledCards[:halfway]
    computerCards = shuffledCards[halfway:]
    allowedCats = ["exercise", "intelligence", "friendliness", "drool"]

    winner = "player"

    while len(playerCards) > 0 and len(computerCards) > 0:
        print(f"PLAYER 1st Card: {playerCards[0]}")
        if winner == "player":
            category = input("Please enter a category: ").lower()
            if category not in allowedCats:
                print("Invalid Category. Returning to menu...")
                return
        else:
            category = random.choice(allowedCats)
            print(f"Computer won the last round and chooses {category}.")
        print(f" COMPUTER 1st Card: {computerCards[0]}")
        playerCard1 = playerCards[0][1][category]
        computerCard1 = computerCards[0][1][category]
        pCard = playerCards[0]
        cCard = computerCards[0]

        if (playerCard1 > computerCard1 and category != "drool") or \
           (playerCard1 < computerCard1 and category == "drool"):
            if category != "drool":
                print("="*40)
                print(f""" PLAYER WINS!
    {category} for {playerCards[0][0]} is greater than {computerCards[0][0]}.""")
            elif category == "drool":
                print("="*40)
                print(f""" PLAYER WINS!
    {category} for {playerCards[0][0]} is less than {computerCards[0][0]}.""")
            playerCards.pop(0)
            computerCards.pop(0)
            playerCards.append(pCard)
            playerCards.append(cCard)
            winner = "player"
            print("="*40)

        elif (computerCard1 > playerCard1 and category != "drool") or \
             (computerCard1 < playerCard1 and category == "drool"):
            if category != "drool":
                print("="*40)
                print(f""" \nCOMPUTER WINS!
    {category} for {computerCards[0][0]} is greater than {playerCards[0][0]}.""")
            elif category == "drool":
                print("="*40)
                print(f""" \nCOMPUTER WINS!
    {category} for {computerCards[0][0]} is less than {playerCards[0][0]}.""")      
            playerCards.pop(0)
            computerCards.pop(0)
            computerCards.append(pCard)
            computerCards.append(cCard)
            winner = "computer"
            print("="*40)

        else:
            print("="*40)
            print(f""" \nIT'S A TIE!
    {category} for {playerCards[0][0]} is the same as {computerCards[0][0]}.
    So the PLAYER WINS!""")
            playerCards.pop(0)
            computerCards.pop(0)
            playerCards.append(pCard)
            playerCards.append(cCard)
            winner = "player"
            print("="*40)

        input("Press enter to go to the next round")
    print("="*40)
    if len(playerCards) > 0:
        print(f"""
\n\t\tTHE PLAYER WINS!
\t\tYOU WON WITH {len(playerCards)} CARDS!""")
    else:
        print(f"""
\n\t\t THE COMPUTER WINS
\t\tIT WON WITH {len(computerCards)} CARDS!
\t\tBetter luck next time...""")
    print("="*40)        
        
    




def menu():
    print("Welcome to Celeb Dogs")
    while True:
        try:
            print("""
\n\t\t1. Play Celeb Dogs
\n\t\t2. Quit""")
            option = int(input("\nPlease choose either option 1 or 2: "))
            if option == 1:
                play()
            elif option == 2:
                quit()
                print("Thank you for playing Celeb Dogs. Press enter to exit")
            else:
                print("Choose option 1 or 2!")
        except ValueError:
            print("Choose a number!")
menu()
