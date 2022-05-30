# Dit is een bestand met allerlei hulpmiddelen.
# Kijk vooral goed welke volgorde de parameters in zitten en welke er zijn.

def button(x, y, breedte, hoogte, kleur, tekst, tekstKleur, tekstFont, tekstGrootte):
    if kleur:
        fill(kleur)
    rect(x,y,breedte,hoogte)
    textAlign(CENTER)
    if tekstFont:
        textFont(tekstFont, tekstGrootte)
    elif tekstGrootte:
        textSize(tekstGrootte)
    if tekstKleur:
        fill(tekstKleur)
    text(tekst, x+(breedte/2), y+(hoogte/2)+tekstGrootte/2)

# Functie om buttons te maken met alles erop en eraan.
# Parameters moeten op de juiste volgorde worden meegegeven.
# Als je geen functie (event listener) toevoegt moet je `None` er invoeren zonder haakjes.
def button2(x, y, breedte, hoogte, kleur, tekst, tekstKleur, tekstFont, tekstGrootte, func):
    if kleur:
        fill(kleur)
    rect(x,y,breedte,hoogte)
    textAlign(CENTER)
    if tekstFont:
        textFont(tekstFont, tekstGrootte)
    elif tekstGrootte:
        textSize(tekstGrootte)
    if tekstKleur:
        fill(tekstKleur)
    text(tekst, x+(breedte/2), y+(hoogte/2)+tekstGrootte/2)
    if mousePressed():
        if x < mouseX < x+breedte and y < mouseY < y+hoogte:
            if func:
                func()

# Functie om iets makkelijker tekst te tonen op het scherm
def drawtext(r, g, b, font, word, x, y):
    fill(r, g, b)
    textFont(font)
    text(word, x, y)
    textAlign(CENTER)

# Functie om buttons met images te tonen op het scherm. Ook deze kan een functie aanroepen
# als je de juiste waardes meegeeft. Je moet ook de breedte en hoogte van de image meegeven
# anders werkt de mousepressed niet.
def imagebutton(img, x, y, hoogte, breedte, func):
    image(img, x, y)
    if mousepressed:
        if x < mouseX < x+breedte and y < mouseY < y+hoogte:
            if func:
                func()
