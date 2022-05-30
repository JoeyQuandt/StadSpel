import backend

def win():
    background(255)
    textAlign(CENTER)
    player = backend.get_player_name(backend.get_current_player())
    text(str(player) + " wins!!", 320, 120)
    fill(0)
    image(loadImage("images/win.jpg"),200,200)
    

    
