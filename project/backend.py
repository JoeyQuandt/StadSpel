# Backend file
# Hierin komt van alles te staan van het geven van de huidige speler
# tot het verwerken van een event. Dit zijn heel veel functies die
# aangeroepen kunnen worden om alle data te krijgen en te verwerken zonder
# dat te doen in de andere bestanden.

# Gebouw constants
FABRIEK = {
    "naam":"Fabriek",
    "energy": -10,
    "cost": 6,
    "population": -3,
    "income": 4,
    "victorypoints": 0
}

HUIS = {
    "naam":"Huis",
    "energy": -5,
    "cost": 3,
    "population": 5,
    "income": 0,
    "victorypoints": 0
}

MONUMENT = {
    "naam":"Monument",
    "energy": 0,
    "cost": 20,
    "population": 0,
    "income": 0,
    "victorypoints": 1
}

ENERGIECENTRALE = {
    "naam":"Energiecentrale",
    "energy": 20,
    "cost": 5,
    "population": -2,
    "income": 0,
    "victorypoints": 0
}

POLITIEBUREAU = {
    "naam":"Politiebureau",
    "energy": -2,
    "cost": 4,
    "population": -2,
    "income": 0,
    "victorypoints": 0
}

BRANDWEERKAZERNE = {
    "naam":"Brandweerkazerne",
    "energy": -2,
    "cost": 4,
    "population": -2,
    "income": 0,
    "victorypoints": 0
}

DAM = {
    "naam":"Dam",
    "energy": -1,
    "cost": 4,
    "population": 0,
    "income": 0,
    "victorypoints": 0
}

currentPlayer = 0
playersAmount = 2
# Player data already set for four players. Turn do not go higher than playersAmount
# So it isn't necessary to have a add_player function
playerData = [{
    "name": "",
    "money": 10,
    "population": 0,
    "energy": 0,
    "income": 0,
    "victorypoints": 0,
    "buildings": [
            HUIS,
            FABRIEK,
            ENERGIECENTRALE
    ]
},
    {
        "name": "",
        "money": 10,
        "population": 0,
        "energy": 0,
        "income":0,
        "victorypoints": 0,
        "buildings": [
            HUIS,
            FABRIEK,
            ENERGIECENTRALE
        ]
    },
    {
        "name": "",
        "money": 10,
        "population": 0,
        "energy": 0,
        "income":0,
        "victorypoints": 0,
        "buildings": [
            HUIS,
            FABRIEK,
            ENERGIECENTRALE
        ]
    },
    {
        "name": "",
        "money": 10,
        "population": 0,
        "energy": 0,
        "income":0,
        "victorypoints": 0,
        "buildings": [
            HUIS,
            FABRIEK,
            ENERGIECENTRALE
        ]
    }
]


# Set the amount of players
def set_amount_of_players(amount):
    global currentPlayer, playersAmount
    playersAmount = amount


# Get the amount of players
def get_amount_of_players():
    global playersAmount
    return playersAmount


# Set a players name
def set_player_name(playerNr, name):
    global playerData
    playerData[playerNr]["name"] = name


# Get a players name
def get_player_name(playerNr):
    global playerData
    return playerData[playerNr]["name"]


# Get the playerNr of the current player
def get_current_player():
    global currentPlayer, playersAmount
    return currentPlayer


# Set the currentPlayer to the next one. If the last player was the last it will go back to the first.
def next_player():
    global currentPlayer, playersAmount
    currentPlayer += 1
    if currentPlayer >= playersAmount:
        currentPlayer = 0


# Set stats to given values
def set_stats(playerNr, energy, population, income, victorypoints):
    global currentPlayer, playersAmount, playerData
    playerData[playerNr]["energy"] = energy
    playerData[playerNr]["population"] = population
    playerData[playerNr]["income"] = income
    playerData[playerNr]["victorypoints"] = victorypoints


# Calculate stats of a given player
def calculate_stats(playerNr):
    global currentPlayer, playersAmount, playerData
    # Make temporary stats for calculating
    tempEnergy = 0
    tempPopulation = 0
    tempIncome = 0
    tempVictoryPoints = 0
    for i in range(0, playerData[playerNr]["buildings"].__len__()):
        tempEnergy += playerData[playerNr]["buildings"][i]["energy"]
        tempPopulation += playerData[playerNr]["buildings"][i]["population"]
        tempIncome += playerData[playerNr]["buildings"][i]["income"]
        tempVictoryPoints += playerData[playerNr]["buildings"][i]["victorypoints"]
    # Set stats to calculated stats
    set_stats(playerNr, tempEnergy, tempPopulation, tempIncome, tempVictoryPoints)
    print(get_stats(playerNr))


# Get all stats of a player
def get_stats(playerNr):
    global currentPlayer, playersAmount, playerData
    return playerData[playerNr]


# Add building to player, use the all caps named variables defined above and the playerNr.
def add_building(playerNr, building):
    global currentPlayer, playerData
    playerData[playerNr]["buildings"].append(building)


# Get buildings of a player
def get_buildings(playerNr):
    global playerData
    return playerData[playerNr]["buildings"]


# Get money from a single player
def get_money(playerNr):
    global currentPlayer, playersAmount
    return playerData[playerNr]["money"]


# Set money of a single player to a wished amount
def set_money(playerNr, amount):
    global currentPlayer, playersAmount, playerData
    playerData[playerNr]["money"] = amount


# Add money to a players current money
def add_money(playerNr, amount):
    set_money(playerNr, get_money(playerNr) + amount)


# Subtract money from a players current money
def subtract_money(playerNr, amount):
    set_money(playerNr, get_money(playerNr) - amount)


# Get population from a single player
def get_population(playerNr):
    global currentPlayer, playersAmount
    return playerData[playerNr]["population"]


# Set population of a single player to a wished amount
def set_population(playerNr, amount):
    global currentPlayer, playersAmount, playerData
    playerData[playerNr]["population"] = amount


# Add population to a players current population
def add_population(playerNr, amount):
    set_population(playerNr, get_population(playerNr) + amount)


# Subtract population from a players current population
def subtract_population(playerNr, amount):
    set_population(playerNr, get_population(playerNr) - amount)


# Get energy from a single player
def get_energy(playerNr):
    global currentPlayer, playersAmount
    return playerData[playerNr]["energy"]


# Set energy of a single player to a wished amount
def set_energy(playerNr, amount):
    global currentPlayer, playersAmount, playerData
    playerData[playerNr]["energy"] = amount


# Add energy to a players current energy
def add_energy(playerNr, amount):
    set_energy(playerNr, get_energy(playerNr) + amount)


# Subtract energy from a players current energy
def subtract_energy(playerNr, amount):
    set_energy(playerNr, get_energy(playerNr) - amount)


# Get victorypoints from a single player
def get_victorypoints(playerNr):
    global currentPlayer, playersAmount
    return playerData[playerNr]["victorypoints"]


# Set victorypoints of a single player to a wished amount
def set_victorypoints(playerNr, amount):
    global currentPlayer, playersAmount, playerData
    playerData[playerNr]["victorypoints"] = amount


# Add victorypoints to a players current victorypoints
def add_victorypoints(playerNr, amount):
    set_victorypoints(playerNr, get_victorypoints(playerNr) + amount)


# Subtract victorypoints from a players current victorypoints
def subtract_victorypoints(playerNr, amount):
    set_victorypoints(playerNr, get_victorypoints(playerNr) - amount)


# Get players income
def get_income(playerNr):
    global playerData
    return playerData[playerNr]["income"]


# Function to check if a player can buy a building
def can_player_buy(playerNr, building):
    canBuy = True
    if get_money(playerNr) < building["cost"]:
        print("Not enough money")
        canBuy = False
    if get_energy(playerNr) - abs(building["energy"]) < 0 and building["energy"] < 0:
        print("Not enough energy")
        canBuy = False
    if get_population(playerNr) - abs(building["population"]) < 0 and building["population"] < 0:
        print("Not enough population")
        canBuy = False

    return canBuy


# Function to check if a player can buy a building
def why_cant_player_buy(playerNr, building):
    reason = ""
    if get_money(playerNr) < building["cost"]:
        reason = "Niet genoeg geld"
    if get_energy(playerNr) - abs(building["energy"]) < 0 and building["energy"] < 0:
        reason = "Niet genoeg energie"
    if get_population(playerNr) - abs(building["population"]) < 0 and building["population"] < 0:
        reason = "Niet genoeg inwoners"
    return reason


# Function to get the amoount of a specific building
def amount_of_buildings(playerNr, building):
    global currentPlayer, playersAmount, playerData
    return get_buildings(playerNr).count(building)


# Function to reset the game
def reset_game():
    global playerData, playersAmount, currentPlayer
    currentPlayer = 0
    playersAmount = 2
    playerData = [{
        "name": "",
        "money": 10,
        "population": 0,
        "energy": 0,
        "income": 0,
        "victorypoints": 0,
        "buildings": [
            HUIS,
            FABRIEK,
            ENERGIECENTRALE
        ]
    },
        {
            "name": "",
            "money": 10,
            "population": 0,
            "energy": 0,
            "income": 0,
            "victorypoints": 0,
            "buildings": [
                HUIS,
                FABRIEK,
                ENERGIECENTRALE
            ]
        },
        {
            "name": "",
            "money": 10,
            "population": 0,
            "energy": 0,
            "income": 0,
            "victorypoints": 0,
            "buildings": [
                HUIS,
                FABRIEK,
                ENERGIECENTRALE
            ]
        },
        {
            "name": "",
            "money": 10,
            "population": 0,
            "energy": 0,
            "income": 0,
            "victorypoints": 0,
            "buildings": [
                HUIS,
                FABRIEK,
                ENERGIECENTRALE
            ]
        }
    ]
    for i in [0, 1, 2, 3]:
        calculate_stats(i)
