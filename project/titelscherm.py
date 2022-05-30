import hulpmiddelen
message=' Over het spel'
message2='  Het "Economie Stadspel" is een spel waarin iedere speler een eigen stad gaat starten.'
message3='  Elke maand krijgt de speler inkomsten en gebeurt er wat in de stad.'
message4='  Wat er gebeurd kan iets goeds zijn maar ook iets slechts. \n De event-kaartjes bepalen wat er gebeurt.'
message5='     druk op spatie om verder te gaan!'
def regelscherm():
    background(240)
    image(loadImage("images/logostad.png"),10,10)    
    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    text(message,308,300)
    textSize(15)
    text(message2,308,330)
    text(message3,275,350)
    text(message4,290,370)
    textSize(20)
    text(message5,300,550)
    strokeWeight(5)
    line(0,238,638,241)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)

def keyTyped():
    return key == " "
