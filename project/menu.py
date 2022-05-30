import hulpmiddelen
message='Menu'
def menu():
    background(240) 
    
    hulpmiddelen.button(115,75,400,60,"#a9a9a9",'  Ga terug',"#000000",None,20)
    hulpmiddelen.button(115,150,400,60,"#a9a9a9",'Shop',"#000000",None,20)
    hulpmiddelen.button(115,225,400,60,"#a9a9a9",'  Reset spel',"#000000",None,20)
    hulpmiddelen.button(115,300,400,60,"#a9a9a9",'Beeindig beurt',"#000000",None,20)
    hulpmiddelen.button(115,375,400,60,"#a9a9a9", 'Handleiding' ,"#000000",None,20)


    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    text(message,304,42)
    strokeWeight(5)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)
    image(loadImage("images/return.png"),220,80,50,50)
    image(loadImage("images/winkelwagen.png"),220,160,50,50)
    image(loadImage("images/reset.png"),220,230,50,50)
