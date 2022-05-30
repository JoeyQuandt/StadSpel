import hulpmiddelen
import backend

def twee_spelers(namen_lijst):
    background(240)
    #Speler 1 en 2

    # If current player? Make the button another color
    if backend.get_current_player() == 0:
        hulpmiddelen.button(15, 10, 200, 40, "#00ff00", namen_lijst[0], "#000000", None, 20)
    else:
        hulpmiddelen.button(15,10,200,40,"#a9a9a9",namen_lijst[0],"#000000",None,20)
    if backend.get_current_player() == 1:
        hulpmiddelen.button(425, 10, 200, 40, "#00ff00", namen_lijst[1], "#000000", None, 20)
    else:
        hulpmiddelen.button(425,10,200,40,"#a9a9a9",namen_lijst[1],"#000000",None,20)
#statieken speler 1 en 2
#statistieken van speler 1
    text('Huizen: ' + str(backend.get_buildings(0).count(backend.HUIS)),50,200)
    text('Fabrieken: ' + str(backend.get_buildings(0).count(backend.FABRIEK)),60,225)
    text('Energiecentralen: ' + str(backend.get_buildings(0).count(backend.ENERGIECENTRALE)),93,250)
    text('Monument: ' + str(backend.get_buildings(0).count(backend.MONUMENT)),63,275)
    text('Dam: ' + str(backend.get_buildings(0).count(backend.DAM)),40,300)
    text('Brandweerkazerne: ' + str(backend.get_buildings(0).count(backend.BRANDWEERKAZERNE)),100,325)
    text('Politiebureau: ' + str(backend.get_buildings(0).count(backend.POLITIEBUREAU)),80,350)
    text('$:',50,75)
    text(str(backend.get_stats(0)["money"]),125,75)
    text('Inwoners:',50,100)
    text(str(backend.get_stats(0)["population"]),125,100)
    text('Energie:',50,125)
    text(str(backend.get_stats(0)["energy"]),125,125)
    text('Inkomen:',50,150)
    text(str(backend.get_stats(0)["income"]),125,150)
    text('V Points:',50,175)
    text(str(backend.get_stats(0)["victorypoints"]),125,175)    
#statistieken van speler 2
    text('Huizen: ' + str(backend.get_buildings(1).count(backend.HUIS)),500,200)
    text('Fabrieken: ' + str(backend.get_buildings(1).count(backend.FABRIEK)),514,225)
    text('Energiecentralen: ' + str(backend.get_buildings(1).count(backend.ENERGIECENTRALE)),540,250)
    text('Monument: ' + str(backend.get_buildings(1).count(backend.MONUMENT)),515,275)
    text('Dam: ' + str(backend.get_buildings(1).count(backend.DAM)),490,300)
    text('Brandweerkazerne: ' + str(backend.get_buildings(1).count(backend.BRANDWEERKAZERNE)),535,325)
    text('Politiebureau: ' + str(backend.get_buildings(1).count(backend.POLITIEBUREAU)),525,350)
    text('$:',500,75)
    text(str(backend.get_stats(1)["money"]),575,75)
    text('Inwoners:',500,100)
    text(str(backend.get_stats(1)["population"]),575,100)
    text('Energie:',500,125)
    text(str(backend.get_stats(1)["energy"]),575,125)
    text('Inkomen:',500,150)
    text(str(backend.get_stats(1)["income"]),575,150)
    text('V Points:',500,175)
    text(str(backend.get_stats(1)["victorypoints"]),575,175)
    #Menu/Event button
    hulpmiddelen.button(435,530,200,60,"#a9a9a9",'Menu',"#000000",None,20)
    image(loadImage("images/menu.png"),440,535,50,50)
    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    strokeWeight(5)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)
    
def drie_spelers(namen_lijst):
    background(240)
    #Speler 1 en 2,3
    if backend.get_current_player() == 0:
        hulpmiddelen.button(5, 10, 200, 40, "#00ff00", namen_lijst[0], "#000000", None, 20)
    else:
        hulpmiddelen.button(5,10,200,40,"#a9a9a9",namen_lijst[0],"#000000",None,20)
    if backend.get_current_player() == 1:
        hulpmiddelen.button(220, 10, 200, 40, "#00ff00", namen_lijst[1], "#000000", None, 20)
    else:
        hulpmiddelen.button(220,10,200,40,"#a9a9a9",namen_lijst[1],"#000000",None,20)
    if backend.get_current_player() == 2:
        hulpmiddelen.button(435, 10, 200, 40, "#00ff00", namen_lijst[2], "#000000", None, 20)
    else:
        hulpmiddelen.button(435,10,200,40,"#a9a9a9",namen_lijst[2],"#000000",None,20)
#statistieken van speler 1
    text('Huizen: ' + str(backend.get_buildings(0).count(backend.HUIS)),50,200)
    text('Fabrieken: ' + str(backend.get_buildings(0).count(backend.FABRIEK)),60,225)
    text('Energiecentralen: ' + str(backend.get_buildings(0).count(backend.ENERGIECENTRALE)),93,250)
    text('Monument: ' + str(backend.get_buildings(0).count(backend.MONUMENT)),63,275)
    text('Dam: ' + str(backend.get_buildings(0).count(backend.DAM)),40,300)
    text('Brandweerkazerne: ' + str(backend.get_buildings(0).count(backend.BRANDWEERKAZERNE)),100,325)
    text('Politiebureau: ' + str(backend.get_buildings(0).count(backend.POLITIEBUREAU)),80,350)
    text('$:',50,75)
    text(str(backend.get_stats(0)["money"]),125,75)
    text('Inwoners:',50,100)
    text(str(backend.get_stats(0)["population"]),125,100)
    text('Energie:',50,125)
    text(str(backend.get_stats(0)["energy"]),125,125)
    text('Inkomen:',50,150)
    text(str(backend.get_stats(0)["income"]),125,150)
    text('V Points:',50,175)
    text(str(backend.get_stats(0)["victorypoints"]),125,175)
#statistieken van speler 2
    text('Huizen: ' + str(backend.get_buildings(1).count(backend.HUIS)),500,200)
    text('Fabrieken: ' + str(backend.get_buildings(1).count(backend.FABRIEK)),514,225)
    text('Energiecentralen: ' + str(backend.get_buildings(1).count(backend.ENERGIECENTRALE)),540,250)
    text('Monument: ' + str(backend.get_buildings(1).count(backend.MONUMENT)),515,275)
    text('Dam: ' + str(backend.get_buildings(1).count(backend.DAM)),490,300)
    text('Brandweerkazerne: ' + str(backend.get_buildings(1).count(backend.BRANDWEERKAZERNE)),535,325)
    text('Politiebureau: ' + str(backend.get_buildings(1).count(backend.POLITIEBUREAU)),525,350)
    text('$:',275,75)
    text(str(backend.get_stats(1)["money"]),350,75)
    text('Inwoners:',275,100)
    text(str(backend.get_stats(1)["population"]),350,100)
    text('Energie:',275,125)
    text(str(backend.get_stats(1)["energy"]),350,125)
    text('Inkomen:',275,150)
    text(str(backend.get_stats(1)["income"]),350,150)
    text('V Points:',275,175)
    text(str(backend.get_stats(1)["victorypoints"]),350,175)
#statistieken van speler 3
    text('Huizen: ' + str(backend.get_buildings(2).count(backend.HUIS)),280,200)
    text('Fabrieken: ' + str(backend.get_buildings(2).count(backend.FABRIEK)),294,225)
    text('Energiecentralen: ' + str(backend.get_buildings(2).count(backend.ENERGIECENTRALE)),320,250)
    text('Monument: ' + str(backend.get_buildings(2).count(backend.MONUMENT)),295,275)
    text('Dam: ' + str(backend.get_buildings(2).count(backend.DAM)),270,300)
    text('Brandweerkazerne: ' + str(backend.get_buildings(2).count(backend.BRANDWEERKAZERNE)),315,325)
    text('Politiebureau: ' + str(backend.get_buildings(2).count(backend.POLITIEBUREAU)),305,350)
    text('$:',500,75)
    text(str(backend.get_stats(2)["money"]),575,75)
    text('Inwoners:',500,100)
    text(str(backend.get_stats(2)["population"]),575,100)
    text('Energie:',500,125)
    text(str(backend.get_stats(2)["energy"]),575,125)
    text('Inkomen:',500,150)
    text(str(backend.get_stats(2)["income"]),575,150)
    text('V Points:',500,175)
    text(str(backend.get_stats(2)["victorypoints"]),575,175)
    #Menu
    hulpmiddelen.button(435,530,200,60,"#a9a9a9",'Menu',"#000000",None,20)
    image(loadImage("images/menu.png"),440,535,50,50)
    fill(96,96,96)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)
    
def vier_spelers(namen_lijst):
    background(240)
    #Speler 1,2,3,4
    if backend.get_current_player() == 0:
        hulpmiddelen.button(5, 10, 150, 30, "#00ff00", namen_lijst[0], "#000000", None, 20)
    else:
        hulpmiddelen.button(5,10,150,30,"#a9a9a9",namen_lijst[0],"#000000",None,20)
    if backend.get_current_player() == 1:
        hulpmiddelen.button(165, 10, 150, 30, "#00ff00", namen_lijst[1], "#000000", None, 20)
    else:
        hulpmiddelen.button(165,10,150,30,"#a9a9a9",namen_lijst[1],"#000000",None,20)
    if backend.get_current_player() == 2:
        hulpmiddelen.button(325, 10, 150, 30, "#00ff00", namen_lijst[2], "#000000", None, 20)
    else:
        hulpmiddelen.button(325,10,150,30,"#a9a9a9",namen_lijst[2],"#000000",None,20)
    if backend.get_current_player() == 3:
        hulpmiddelen.button(485, 10, 150, 30, "#00ff00", namen_lijst[3], "#000000", None, 20)
    else:
        hulpmiddelen.button(485,10,150,30,"#a9a9a9",namen_lijst[3],"#000000",None,20)
    #Statieken 1,2,3,4
    #statistieken van speler 1
    text('Huizen: ' + str(backend.get_buildings(0).count(backend.HUIS)),50,200)
    text('Fabriek: ' + str(backend.get_buildings(0).count(backend.FABRIEK)),50,225)
    text('Energie: ' + str(backend.get_buildings(0).count(backend.ENERGIECENTRALE)),50,250)
    text('Monument: ' + str(backend.get_buildings(0).count(backend.MONUMENT)),70,275)
    text('Dam: ' + str(backend.get_buildings(0).count(backend.DAM)),40,300)
    text('Brandweer: ' + str(backend.get_buildings(0).count(backend.BRANDWEERKAZERNE)),65,325)
    text('Politie: ' + str(backend.get_buildings(0).count(backend.POLITIEBUREAU)),50,350)
    text('$:',50,75)
    text(str(backend.get_stats(0)["money"]),125,75)
    text('Inwoners:',50,100)
    text(str(backend.get_stats(0)["population"]),125,100)
    text('Energie:',50,125)
    text(str(backend.get_stats(0)["energy"]),125,125)
    text('Inkomen:',50,150)
    text(str(backend.get_stats(0)["income"]),125,150)
    text('V Points:',50,175)
    text(str(backend.get_stats(0)["victorypoints"]),125,175)
    #statistieken van speler 2
    text('Huizen: ' + str(backend.get_buildings(1).count(backend.HUIS)),200,200)
    text('Fabriek: ' + str(backend.get_buildings(1).count(backend.FABRIEK)),200,225)
    text('Energie: ' + str(backend.get_buildings(1).count(backend.ENERGIECENTRALE)),200,250)
    text('Monument: ' + str(backend.get_buildings(1).count(backend.MONUMENT)),220,275)
    text('Dam: ' + str(backend.get_buildings(1).count(backend.DAM)),200,300)
    text('Brandweer: ' + str(backend.get_buildings(1).count(backend.BRANDWEERKAZERNE)),215,325)
    text('Politie: ' + str(backend.get_buildings(1).count(backend.POLITIEBUREAU)),200,350)
    text('$:',200,75)
    text(str(backend.get_stats(1)["money"]),275,75)
    text('Inwoners:',200,100)
    text(str(backend.get_stats(1)["population"]),275,100)
    text('Energie:',200,125)
    text(str(backend.get_stats(1)["energy"]),275,125)
    text('Inkomen:',200,150)
    text(str(backend.get_stats(1)["income"]),275,150)
    text('V Points:',200,175)
    text(str(backend.get_stats(1)["victorypoints"]),275,175)
    #statistieken van speler 3
    text('Huizen: ' + str(backend.get_buildings(2).count(backend.HUIS)),350,200)
    text('Fabriek: ' + str(backend.get_buildings(2).count(backend.FABRIEK)),350,225)
    text('Energie: ' + str(backend.get_buildings(2).count(backend.ENERGIECENTRALE)),350,250)
    text('Monument: ' + str(backend.get_buildings(2).count(backend.MONUMENT)),370,275)
    text('Dam: ' + str(backend.get_buildings(2).count(backend.DAM)),350,300)
    text('Brandweer: ' + str(backend.get_buildings(2).count(backend.BRANDWEERKAZERNE)),365,325)
    text('Politie: ' + str(backend.get_buildings(2).count(backend.POLITIEBUREAU)),350,350)
    text('$:',350,75)
    text(str(backend.get_stats(2)["money"]),425,75)
    text('Inwoners:',350,100)
    text(str(backend.get_stats(2)["population"]),425,100)
    text('Energie:',350,125)
    text(str(backend.get_stats(2)["energy"]),425,125)
    text('Inkomen:',350,150)
    text(str(backend.get_stats(2)["income"]),425,150)
    text('V Points:',350,175)
    text(str(backend.get_stats(2)["victorypoints"]),425,175)
    #statistieken van speler 4
    text('Huizen: ' + str(backend.get_buildings(3).count(backend.HUIS)),530,200)
    text('Fabriek: ' + str(backend.get_buildings(3).count(backend.FABRIEK)),530,225)
    text('Energie: ' + str(backend.get_buildings(3).count(backend.ENERGIECENTRALE)),530,250)
    text('Monument: ' + str(backend.get_buildings(3).count(backend.MONUMENT)),550,275)
    text('Dam: ' + str(backend.get_buildings(3).count(backend.DAM)),530,300)
    text('Brandweer: ' + str(backend.get_buildings(3).count(backend.BRANDWEERKAZERNE)),545,325)
    text('Politie: ' + str(backend.get_buildings(3).count(backend.POLITIEBUREAU)),530,350)
    text('$:',525,75)
    text(str(backend.get_stats(3)["money"]),600,75)
    text('Inwoners:',525,100)
    text(str(backend.get_stats(3)["population"]),600,100)
    text('Energie:',525,125)
    text(str(backend.get_stats(3)["energy"]),600,125)
    text('Inkomen:',525,150)
    text(str(backend.get_stats(3)["income"]),600,150)
    text('V Points',525,175)
    text(str(backend.get_stats(3)["victorypoints"]),600,175)
    #Menu
    hulpmiddelen.button(435,530,200,60,"#a9a9a9",'Menu',"#000000",None,20)
    image(loadImage("images/menu.png"),440,535,50,50)
    fill(96,96,96)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)
