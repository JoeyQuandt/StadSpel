import random, backend, hulpmiddelen
                        
#Genereer nieuw random event
def new_random_event():
    global chosenPlayer, currentPlayer, event, showEventState, eventImg
    events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    event = random.choice(events)
    eventName = "" 
    
    currentPlayer = backend.currentPlayer
    currentTotalPlayers = backend.playersAmount
    currentBuildings = backend.get_buildings(currentPlayer)
    showEventState = True
    eventImg = loadImage("images/eventkaartjes/event"+ str(event) + ".jpg")
    
    #Pas statistieken aan
    if event == 1:                           # Je ontvangt $5
        eventName = "Geluksdag"
        backend.add_money(currentPlayer, 5)
        
    if event == 2:                           # Alle spelers ontvangen $2
        eventName = "Goede maand"
        playerCounter = 0
        while playerCounter < currentTotalPlayers:
            backend.add_money(playerCounter, 2)
            playerCounter += 1
            
    if event == 3:                           # Je krijgt +2 inwoners
        eventName = "Immigratie"
        backend.add_population(currentPlayer, 2)

    if event == 4:                           # Je verdubbelt je geld, maar je fabrieken verdienen geen geld deze beurt
        eventName = "Loterij"
        currentStats = backend.get_stats(currentPlayer)
        currentMoney = backend.get_money(currentPlayer)
        if currentMoney < 0:
            multipliedMoney = currentMoney / 2
        else: 
            multipliedMoney = currentMoney * 2
        backend.set_stats(currentPlayer, currentStats["energy"], currentStats["population"], 0, currentStats["victorypoints"])
        backend.set_money(currentPlayer, multipliedMoney)
        
    if event == 5:                           # Kies een andere speler, die speler verliest $2
        eventName = "Crisis (andere stad)"
        choose_player()
        
    if event == 6:                           # Je mag $5 stelen van een andere speler (Politiebureau voorkomt dit)
        eventName = "Diefstal"
        choose_player()
        
    if event == 7:                          # Je verliest $6 (Politie voorkomt dit)
        eventName = "Hooligans"
        if "Politiebureau" not in str(currentBuildings):
            backend.subtract_money(currentPlayer, 6)
        else:
            print("Je politiebureau is dit tegen gegaan!")
            
    if event == 8:                          # Je verliest $2
        eventName = "Crisis (eigen stad)"
        backend.subtract_money(currentPlayer, 2)
            
    if event == 9:                          # Je moet $2 aan alle spelers betalen
        eventName = "Goede doel"        
        backend.subtract_money(currentPlayer, (currentTotalPlayers * 2))
        playerCounter = 0
        while playerCounter < currentTotalPlayers:
            backend.add_money(playerCounter, 2)
            playerCounter += 1
            
    if event == 10:                          # Je moet je beurt overslaan (Je mag NIET bouwen en je krijgt GEEN geld)
        eventName = "Tijdstop"
        backend.next_player()
        
    if event == 11:                          # Je verliest $8 (Brandweer voorkomt dit)
        eventName = "Bank brand"
        if "Brandweerkazerne" not in str(currentBuildings):
            backend.subtract_money(currentPlayer, 8)
        else:
            print("Je brandweerkazerne is dit tegen gegaan!")
            
    if event == 12:                          # Je verliest $10 (Dam voorkomt dit)
        eventName = "Overstroming"
        if "Dam" not in str(currentBuildings):
            backend.subtract_money(currentPlayer, 10)
        else:
            print("Je dam is dit tegen gegaan!")
            
    if event == 13:                          # Er gebeurt niets bijzonders in je stad
        eventName = "Rustige maand"
    
    print(eventName)

#Kies een speler
def choose_player():
    global showPlayerChooseButtons
    showPlayerChooseButtons = True

def player_is_chosen():
    if event == 5:
        event5()
    if event == 6:
        event6()

def event5():
    #Haal geld van de gekozen speler af
    backend.subtract_money(chosenPlayer, 2)
    
def event6():
    #Check of speler een politiebureau heeft
    if "Politiebureau" not in str(backend.get_buildings(chosenPlayer)):
        backend.subtract_money(chosenPlayer, 5)
        backend.add_money(currentPlayer, 5)
    else: 
        print("Het politiebureau van de andere speler is dit tegen gegaan!")
