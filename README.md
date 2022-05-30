# StadSpel

Het stadspel is een project van het eerste jaar, tweede periode van informatica aan de Hogeschool Rotterdam.
In deze README komt allemaal informatie te staan over hoe het dev team dingen moet/kan doen.

## Classes 

We gaan werken met classes. Is niet zo moeilijk als je zal denken en de classes hoef je niet zelf te maken. classes worden altijd met een hoofdletter als eerste letter geschreven. Als je een class toe wijst aan een variabel en hem daar initialiseerd door Classnaam() te typen word het een object.

### Spelers

In plaats van variabel speler1, speler2, speler3 en speler4 hebben we een array spelers[] met daarin Speler objecten.
het Speler object heeft een aantal functies om data op te vragen en een aantal oom data te wijzigen. 

Getters (Functies die data ophalen):
- getGeld()
- getEnergie()
- getInwoners()
- getGebouwen()

Setters (Functies die data wijzigen):
- Nog geen

### Gebouwen

Gebouwen zijn ook classes. deze hebben ook een aantal functies en wat meer data die vast staat. Als je in gebouwen.py kijkt zal je zien dat een gebouw in de __init__() allemaal data heeft. Deze data staat vast en veranderd niet. Dit zijn de basis gegevens van de gebouwen zoals kosten, naam, inwoners etc. Deze getallen kunnen ook negatief zijn maar zijn wel altijd een int. 

GetNaam() lijkt misschien raar, waarom zou je elke keer die functie schrijven als je ook het in een string kan typen? Dat is omdat het best practice is. Als we om wat voor reden dan ook besluiten om de naam te veranderen dan hoef je dat maar op één plek te doen in plaats van in al je strings.

Getters:
- getNaam()
- getKosten()

## Hulpmiddelen

Uiteraard moet het makkelijk voor ons zijn. Ik ga in de loop van het project ook wat hulpmiddelen toevoegen. De eerste daarvan is een functie om makkelijk buttons te maken. deze staan in het hulpmiddelen.py bestand en die moet geimporteerd zijn door middel van `import hulpmiddelen as hm`. En dan kan je de functies aanroepen zoals dit: `hm.button(params...)`. 

De volgende hulpmiddelen zijn er:

- button(x*, y*, breedte*, hoogte*, kleur, tekst*, tekstKleur, tekstFont, tekstGrootte, functie)

* De parameters met een ster* zijn niet verplicht. Type `None` als je deze niet wilt invullen.

### Button

De parameters zijn er veel in deze functie. de x,y,breedte en hoogte spreken voor zich. De kleur en tekstKleur zijn kleur waardes die processing snapt, zoals Hex (#00ff00). tekstFont is een font die processing snapt. tekstgrootte en tekst spreken voor zich lijkt mij ook. Functie is een parameter waar je een functie kan meegeven. Deze functie word aangeroepen wanneer er op de knop word geklikt. deze geef je mee door de functie naam **zonder** haakjes erachter neer te zetten. als je geen functie hebt of als je eerst de button wilt plaatsen type je `None` of `False` (Met hoofdletter)


