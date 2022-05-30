import hulpmiddelen
def shop():
    background(240)
    hulpmiddelen.button(435,530,200,60,"#a9a9a9",'Menu',"#000000",None,20)
    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    strokeWeight(5)
    line(0,238,638,241)
    #Bottom
    fill(0)
    rect(0,600,640,40,7)

    image(loadImage("images/shop.png"),170,10, 300, 200)
    image(loadImage("images/huis.jpg"),0,250,121,122)
    image(loadImage("images/fabriek2.jpg"),150,250,121,122)
    image(loadImage("images/fabriek1.jpg"),300,250,121,122)
    image(loadImage("images/dam.png"), 450, 250, 121, 122)
    image(loadImage("images/politie.png"), 0, 400, 121, 122)
    image(loadImage("images/brandweer.png"), 150, 400, 121, 122)
    image(loadImage("images/monument.png"), 300, 400, 121, 122)
    
