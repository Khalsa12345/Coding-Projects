def airportDetails():
    airportUK = input("Please enter the 3 letter airport code for the UK airport: ").upper()
    allowedUKAirports = ["LPL", "BOH"]
    if airportUK not in allowedUKAirports:
        print("Not a Valid Airport.\nReturning to menu...")
        return "", "", {}
    airportInt = input("Please enter the 3 letter airport code for the international airport: ").upper()
    allowedIntAirports = open("Airports.txt", "r")
    intAirports = {}
    for line in allowedIntAirports:
        airport, airportFull, distanceLPL, distanceBOH  = line.strip().split(",")
        intAirports[airport] = [airportFull, int(distanceLPL), int(distanceBOH)]
    if airportInt not in intAirports:
        print("Not a valid International Airport. \nReturning to menu...")
        return "", "", {}
    print(f"Airport Name: {intAirports[airportInt][0]}")
    allowedIntAirports.close()
    return airportUK, airportInt, intAirports

def flightDetails():
    allowedAircraft = {
        "MNB" : [8, 2650, 180, 8],
        "LNB" : [7, 5600, 220, 10],
        "MWB" : [5, 4050, 406, 14]}
    aircraftType = input("Please enter a valid aircraft type (Abbreviation): ").upper()
    if aircraftType not in allowedAircraft:
        print("Invalid Aircraft Type, \nReturning to menu...")
        return "", None, {}, None
    print(f"""
Aircraft Details:
\n\t{aircraftType}:
\tRunning cost per seat per 100km: £{allowedAircraft[aircraftType][0]}
\tMaximum Flight Range: {allowedAircraft[aircraftType][1]}km
\tCapacity if all seats are standard-class: {allowedAircraft[aircraftType][2]}
\tMinimum number of first-class seats (if there are any): {allowedAircraft[aircraftType][3]}""")
    try:
        firstClassSeats = int(input("Enter the number of first class seats: "))
    except ValueError:
        print("Enter a number! \nReturning to menu...")
        return "", None, {}, None
    if firstClassSeats != 0:
        if firstClassSeats < allowedAircraft[aircraftType][3]:
            print("Invalid Amount. \nReturning to menu...")
            return "", None, {}, None
        elif firstClassSeats > allowedAircraft[aircraftType][2]:
            print("Invalid Amount. \nReturning to menu...")
            return "", None, {}, None
    standardSeats = allowedAircraft[aircraftType][2] - firstClassSeats * 2
    print(f"Number of standard seats: {standardSeats}")
    return aircraftType, firstClassSeats, allowedAircraft, standardSeats

def pricePlan(flightData):

    if "airportUK" not in flightData or flightData["airportUK"] == "":
        print("No airport options entered. \nReturning to menu...")
        return 
    if "aircraftType" not in flightData or flightData["aircraftType"] == "":
        print("No aircraft option entered. \nReturning to menu...")
        return 
    if "firstClassSeats" not in flightData or flightData["firstClassSeats"] is None:
        print("No number of first class seats entered. \nReturning to menu...")
        return
    if flightData["airportUK"] == "LPL":
        num = 1
    else:
        num = 2
    chosenAircraft = flightData["aircraftType"]
    chosenAirport = flightData["airportInt"]
    maxRange = flightData["allowedAircraft"][chosenAircraft][1]
    flightDistance = flightData["intAirports"][chosenAirport][num]
    if maxRange < flightDistance:
        print("The distance from the UK airport to the international airport is too large. \nReturning to menu...")
        return
    try:
        sSeatPrice = int(input("What is the price of a standard seat? "))
        fSeatPrice = int(input("What is the price of a first class seat? "))
        runningCost = int(flightData["allowedAircraft"][chosenAircraft][0])
        flightCostPerSeat = runningCost * int(flightDistance) / 100
        flightCost = flightCostPerSeat * (flightData["firstClassSeats"] + flightData["standardSeats"])
        flightIncome = flightData["firstClassSeats"] * fSeatPrice + flightData["standardSeats"] * sSeatPrice   
        flightProfit = flightIncome - flightCost
        print(f"""
    Flight cost per seat: £{flightCostPerSeat}
    Flight cost: £{flightCost}
    Flight Income: £{flightIncome}
    flight Profit: £{round(flightProfit, 0)}""")
    except ValueError:
        print("Invalid numbers entered! \nReturning to menu...")
        return
    

def clear(flightData):
    flightData["airportUK"] = ""
    flightData["airportInt"] = ""
    flightData["intAirports"] = {}
    flightData["aircraftType"] = ""
    flightData["firstClassSeats"] = None
    flightData["allowedAircraft"] = {}
    flightData["standardSeats"] = None
    print("All data Cleared! \nReturning to menu...")



def menu():
    airportUK = ""
    airportInt = ""
    aircraftType = ""
    firstClassSeats = 0
    flightData = {}
    print("Welcome to the airport profit checker")
    while True:
        print("""
\n\t 1. Enter Airport Details
\t 2. Enter Flight Details
\t 3. Enter Price Plan and Calculate Profit
\t 4. Clear Data
\t 5. Quit""")
        try:
            option = int(input("\nPlease Choose from option 1-5: "))
            if option == 1:
                flightData["airportUK"], flightData["airportInt"], flightData["intAirports"] = airportDetails()
            elif option == 2:
                flightData["aircraftType"],flightData["firstClassSeats"], flightData["allowedAircraft"], flightData["standardSeats"] = flightDetails()
            elif option == 3:
                pricePlan(flightData)
            elif option == 4:
                clear(flightData)
            elif option == 5:
                print("Thank you for using the airport profit checker. Press enter to exit.")
                quit()
            else:
                print("Invalid Option. Choose from 1-5!")
        except ValueError:
            print("Choose a Number!")
    
menu()
