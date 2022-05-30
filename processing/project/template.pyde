def setup():
    global img,message
    size(640,640)
    img=loadImage("logostad.png")
    message='Kies hier in hoeveel spelers je hebt:'

def draw():
    global img,message
    background(240)
    #Message
    textAlign(CENTER)
    fill(96,96,96)
    textSize(30)
    text(message,width/2,height/2)
    #Image and line
    image(img,10,10)
    strokeWeight(5)
    line(0,238,638,241)
    #Bottom
    rect(0,600,640,40,7)
