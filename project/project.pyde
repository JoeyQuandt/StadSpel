import hulpmiddelen,random,titelscherm,spelerskeuzenmenu,spelers_pagina,webshop,menu, naam_invul, backend, eventkaartjes, overwinningsscherm,  handleiding


def setup():
    global state,playercount,message2 ,namen_lijst, naam_input, speler, status, waarde, eventIsClicked
    size(640,640)
    state=0
    playercount=0
    namen_lijst = []
    naam_input = ""
    waarde = ""
    status = ""

    speler = backend.get_stats(backend.get_current_player())
    playersAmount = backend.playersAmount
    eventkaartjes.showEventState = False
    eventkaartjes.showPlayerChooseButtons = False
    eventkaartjes.chosenPlayer = 0
    eventIsClicked = False

    message2 = "Klik hier voor event"
    for i in [0,1,2,3]:
        backend.calculate_stats(i)

def mousePressed():
    global state, playercount, message2, naam_input, namen_lijst,status, waarde, eventIsClicked
    
    # Menu button om terug te gaan naar de spelerspagina "Ga terug"
    if 115<mouseX<515 and 75<mouseY<135 and state==7:
        if backend.get_amount_of_players()==2:
            state=2
        elif backend.get_amount_of_players()==3:
            state=3
        elif backend.get_amount_of_players()==4:
            state=4
            
    # Menu button naar de shop te gaan
    elif 115<mouseX<515 and 150<mouseY<210 and state==7:
        state=5

        
    # Menu button die terug gaat naar het spelerkeuzenmenu en reset het spel.
    elif 115<mouseX<515 and 225<mouseY<285 and state==7:
        state=1
        namen_lijst=[]
        naam_input=""
        eventIsClicked = False
        eventkaartjes.showEventState = False
        eventkaartjes.showPlayerChooseButtons = False
        backend.reset_game()
        #115,375,400,60


    elif 115<mouseX<515 and 375 < mouseY < 435 and state == 7:
        state = 10


    if state == 10:
        handleiding.handleiding()
        if 0<mouseX<250 and 530<mouseY<590:
            if backend.get_amount_of_players()==2:
                state=2
            elif backend.get_amount_of_players()==3:
                state=3
            elif backend.get_amount_of_players()==4:
                state=4



    # Beeindig beurt
    elif 115 < mouseX < 515 and 300<mouseY < 360 and state ==7:
        if eventIsClicked == True:
            backend.add_money(backend.get_current_player(), backend.get_income(backend.get_current_player()))
        
            eventIsClicked = False
            eventkaartjes.showEventState = False
            eventkaartjes.showPlayerChooseButtons = False
            backend.next_player()
            
            if backend.get_stats(backend.get_current_player())["victorypoints"]>=3:
                state=9
            elif backend.get_amount_of_players()==2:
                state=2
            elif backend.get_amount_of_players()==3:
                state=3
            elif backend.get_amount_of_players()==4:
                state=4
            
    #2 spelers pagina
    elif 8<mouseX<158 and 400<mouseY<480 and state==1:
        state=2
        backend.set_amount_of_players(2)
    #3 spelers pagina
    elif 240<mouseX<390 and 400<mouseY<480 and state==1:
        state=3
        backend.set_amount_of_players(3)
    #4 spelers pagina
    elif 480<mouseX<630 and 400<mouseY<480 and state==1:
        state=4
        backend .set_amount_of_players(4)
    #menu
    elif 435<mouseX<635 and 530<mouseY<590:
        state=7
    #event
    elif 0<mouseX<250 and 530<mouseY<590:
        if (state == 2 or state == 3 or state == 4) and eventIsClicked == False:
            eventkaartjes.new_random_event()
            eventIsClicked = True
            if eventkaartjes.event == 10:
                eventIsClicked = False

                                      #huis
    if state==5 and isMouseWithinImage(0,250,121,122):
        print("click")
        status = "Je hebt een huis gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.HUIS):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.HUIS)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.HUIS["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.HUIS)
            backend.calculate_stats(backend.get_current_player())
                                      #fabriek
    if state==5 and isMouseWithinImage(300,250,121,122):
        print("click")
        status = "Je hebt een fabriek gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.FABRIEK):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.FABRIEK)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.FABRIEK["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.FABRIEK)
            backend.calculate_stats(backend.get_current_player())
                                      #energiecentrale
    if state==5 and isMouseWithinImage(150,250,121,122):
        print("click")
        status = "Je hebt een energiecentrale gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.ENERGIECENTRALE):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.ENERGIECENTRALE)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.ENERGIECENTRALE["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.ENERGIECENTRALE)
            backend.calculate_stats(backend.get_current_player())
                                          #dam
    if state==5 and isMouseWithinImage(450, 250, 121, 122):
        print("click")
        status = "Je hebt een dam gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.DAM):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.DAM)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.DAM["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.DAM)
            backend.calculate_stats(backend.get_current_player())
                                         #politie
    if state==5 and isMouseWithinImage(0, 400, 121, 122):
        print("click")
        status = "Je hebt een politiebureau gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.POLITIEBUREAU):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.POLITIEBUREAU)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.POLITIEBUREAU["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.POLITIEBUREAU) 
            backend.calculate_stats(backend.get_current_player())
                                           #monument
    if state==5 and isMouseWithinImage(300, 400, 121, 122):
        print("click")
        status = "Je hebt een monument gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.MONUMENT):
            status = backend.why_cant_player_buy(backend.get_current_player(),backend.MONUMENT)
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.MONUMENT["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.MONUMENT) 
            backend.calculate_stats(backend.get_current_player())
                                            #brandweer
    if state==5 and isMouseWithinImage(150, 400, 121, 122):
        print("click")
        status = "Je hebt een brandweerkazerne gekocht."
        if eventIsClicked == False:
            status = "Pak eerst een event kaart!"
        elif not backend.can_player_buy(backend.get_current_player(), backend.BRANDWEERKAZERNE):
            status = "Je kunt dit item nog niet kopen."
            print(status)
        else:
            backend.subtract_money(backend.get_current_player(), backend.BRANDWEERKAZERNE["cost"])
            print(speler["money"])
            backend.add_building(backend.get_current_player(), backend.BRANDWEERKAZERNE)
            backend.calculate_stats(backend.get_current_player())


    #Knoppen voor een player te kiezen
    if eventkaartjes.showPlayerChooseButtons == True:
        if backend.playersAmount >= 2:
            if 300<mouseX<400 and 400<mouseY<450:
                print("Player 1")
                eventkaartjes.chosenPlayer = 0
                eventkaartjes.showPlayerChooseButtons = False
                eventkaartjes.player_is_chosen()
            if 300<mouseX<400 and 450<mouseY<500:
                print("Player 2")
                eventkaartjes.chosenPlayer = 1
                eventkaartjes.showPlayerChooseButtons = False
                eventkaartjes.player_is_chosen()
            if backend.playersAmount >= 3:
                if 400<mouseX<500 and 400<mouseY<450:
                    print("Player 3")
                    eventkaartjes.chosenPlayer = 2
                    eventkaartjes.showPlayerChooseButtons = False
                    eventkaartjes.player_is_chosen()
                if backend.playersAmount >= 4:
                    if 400<mouseX<500 and 450<mouseY<500:
                        print("Player 4")
                        eventkaartjes.chosenPlayer = 3
                        eventkaartjes.showPlayerChooseButtons = False
                        eventkaartjes.player_is_chosen()

def draw():
    global state, playercount, namen_lijst, naam_input, waarde, status
    #Begin scherm
    if state==0:
        titelscherm.regelscherm()
        if titelscherm.keyTyped():
            state=1
    #Keuze menu voor welke spelers je kan kiezen
    elif state==1:
        spelerskeuzenmenu.pagina1()
        
    #Pagina 1 als je 2 speler kiest
    elif state==2 and backend.get_amount_of_players()==2:
        
        # print(backend.get_player_name(0))
        naam_invul.scherm(naam_input)

        if len(namen_lijst) == backend.get_amount_of_players()==2:
            for x in range(2):
                backend.set_player_name(x, namen_lijst[x])


            spelers_pagina.twee_spelers(namen_lijst)
            if eventkaartjes.showEventState == True:
                image(eventkaartjes.eventImg, 50, 360, 150, 200)
            event_show()
    #Pagina 2 als je 3 spelers kiest
    elif state==3 and backend.get_amount_of_players()==3:
        
        naam_invul.scherm(naam_input)
        if len(namen_lijst) == backend.get_amount_of_players()==3:
            for x in range(3):
                backend.set_player_name(x, namen_lijst[x])
            spelers_pagina.drie_spelers(namen_lijst)
            if eventkaartjes.showEventState == True:
                image(eventkaartjes.eventImg, 50, 360, 150, 200)
            event_show()
    #Pagina 3 als je 4 spelers kiest
    elif state==4 and backend.get_amount_of_players()==4:
        naam_invul.scherm(naam_input)
        if len(namen_lijst) == backend.get_amount_of_players()==4:
            for x in range(4):
                backend.set_player_name(x, namen_lijst[x])
            spelers_pagina.vier_spelers(namen_lijst)
            if eventkaartjes.showEventState == True:
                image(eventkaartjes.eventImg, 50, 360, 150, 200)
            event_show()


    #Webshop
    elif state==5:
        webshop.shop()
        textSize(32)
        text(str(waarde), 400, 100) #geld, inwoners, energie / moet nog input krijgen via backend /
        textSize(20)
        text(str(status), 325, 200) #kan je het kopen ja of nee?
    #Menu
    elif state==7:
        menu.menu()
    elif state==8:
        pass
    elif state==9:
        overwinningsscherm.win()
        
def event_show():
    hulpmiddelen.button(0,530,250,60,"#a9a9a9",message2,"#00000",None,20)

    #Laat een keuze menu zien met de huidige spelers 
    if eventkaartjes.showPlayerChooseButtons == True:
        if backend.playersAmount >= 2:
            buttonP1 = hulpmiddelen.button(300,400,100,50,"#a9a9a9","Player 1","#00000",None,20)
            buttonP2 = hulpmiddelen.button(300,450,100,50,"#a9a9a9","Player 2","#00000",None,20)
            if backend.playersAmount >= 3:
                buttonP3 = hulpmiddelen.button(400,400,100,50,"#a9a9a9","Player 3","#00000",None,20)
                if backend.playersAmount >= 4:
                    buttonP4 = hulpmiddelen.button(400,450,100,50,"#a9a9a9","Player 4","#00000",None,20)

def keyTyped():
    global namen_lijst, naam_input, playercount, state
    # Maakt een naam alleen als de states 2, 3 of 4 is
    if state == 2 or state == 3 or state == 4:
        # Voegt de naam alleen toe als de naam niet leeg is of een enter
        if key == "\n" and naam_input != "" and naam_input != "\n":
            namen_lijst.append(naam_input.encode("ascii"))



            naam_input = ""
        # Verwijderd een character als je backspace indrukt
        elif key == "\x08" or naam_input == "\n":
            naam_input = naam_input[:-1]
        # Zorgt ervoor dat je niet alleen spaties als naam kan gebruiken.
        elif naam_input.isspace():
            naam_input = naam_input[:-1]
        else:
            naam_input+= key        
            
            
def isMouseWithinImage(x, y, breedte, hoogte): #kleine def om de shop te laten functioneren.
    if x < mouseX < x + breedte and y < mouseY < y + hoogte:
        return True
    else:
        return False
