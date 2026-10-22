def set_gen0():
    population = []
    survivalRate = []
    birthRate = 0
    numOfGens = 0
    print("")
    print("You will now be asked to set the generation 0 values.")
    print("")
    popJ = int(input("Please enter the number of juveniles: "))
    popA = int(input("Please enter the number of adults: "))
    popS = int(input("Please enter the number of seniles: "))
    population.extend([popJ, popA, popS])
    SRJ = float(input("Please enter the survival rate for juveniles (Between 0-1): "))
    SRA = float(input("Please enter the survival rate for adults (Between 0-1) : "))
    SRS = float(input("Please enter the survival rate for seniles (Between 0-1) : "))
    survivalRate.extend([SRJ, SRA, SRS])
    birthRate = float(input("Please enter the birth rate (Adults): "))
    while True:
        numOfGens = int(input("Please enter the number of generations you want it to run through (Between 5-25) :"))
        if 5<= numOfGens <=25:
            break
        else:
            print("Error! Please enter a value between 5 and 25!")
    total = popJ + popA + popS
    print("Success!")


    return [popJ, popA, popS, SRJ, SRA, SRS, birthRate, numOfGens, total]
#Shortened name for Returned Variables - I've turned all returned
#variables into a list and to call them, pull out the index value
#as rVrs[index value] in order. rVrs[2] will pull out popS and
#rVrs[7] will pull out numOfGens
rVrs =[]

def disp_gen0():
    print(f'''
Population of Juveniles: {rVrs[0]}
Population of Adults: {rVrs[1]}
Population of Seniles: {rVrs[2]}

Survival Rate for Juveniles: {rVrs[3]}
Survival Rate for Adults: {rVrs[4]}
Survival Rate for Seniles: {rVrs[5]}

Birth Rate (for Adults): {rVrs[6]}

Number of generations to run through: {rVrs[7]}''')

def model():
    cPopJ = rVrs[0]
    cPopA = rVrs[1]
    cPopS = rVrs[2]
    cSRJ = rVrs[3]
    cSRA = rVrs[4]
    cSRS = rVrs[5]
    cBirthRate = rVrs[6]
    print(f'''
Generation \tJuveniles \tAdults \t\tSeniles \tTotal

Generation 0 \t{rVrs[0]} \t\t{rVrs[1]} \t\t{rVrs[2]} \t\t{rVrs[8]}''')
    for gen in range(1, rVrs[7] + 1):
        newPopA = round(cPopJ * cSRJ)
        newPopS = round(cPopA * cSRA) + round(cPopS * cSRS)
        births = round(cPopA * cBirthRate)
        cPopJ = births
        cPopA = newPopA
        cPopS = newPopS
        cTotal = cPopJ + cPopA + cPopS
        print(f'''
Generation {gen} \t{cPopJ} \t\t{cPopA} \t\t{cPopS} \t\t{cTotal}''')
        
        


while True:
    print('''Main Menu
        1. Set Generation 0 Values
        2. Display Generation 0 Values
        3. Run The Model
        4. Exit''')
    choice = int(input("Please enter the option number: "))
    if choice == 1:
        rVrs = set_gen0()
    elif choice == 2:
        if rVrs == []:
            print("No Values! Please enter the values for generation 0")
        else:
            disp_gen0() 
    elif choice == 3:
        if rVrs == []:
            print("No Values! Please enter the values for generation 0")
        else:
            model()
    elif choice == 4:
        print("Thank you for using The Greenfly Model. Press Enter to exit")
        quit()
    else:
        print("Not an option. Choose a number from 1-4")
        

    
