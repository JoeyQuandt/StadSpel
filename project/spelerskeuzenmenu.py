import hulpmiddelen

message='Kies hier hoeveel spelers je hebt:'
state=0
playercount=0
    
def pagina1():
    background(240)
    image(loadImage("images/logostad.png"),10,10)

    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    text(message,width/2,height/2)
    hulpmiddelen.button(8,400,150,80,"#a9a9a9",'2 spelers',"#000000",None,32)
    hulpmiddelen.button(240,400,150,80,"#a9a9a9",'3 spelers',"#000000",None,32)
    hulpmiddelen.button(480,400,150,80,"#a9a9a9",'4 spelers',"#000000",None,32)
    strokeWeight(5)
    line(0,238,638,241)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)
    

    
    
