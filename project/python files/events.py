# In deze class staat alle data voor de events.
# Bij het aanmaken van een nieuw event word er meteen een random event geactiveerd.

import random

class Event:
    # Initialiseer een event met een speler er aan gekoppeld
    def __init__(self, speler):
        self.speler = speler
        # Activeer een event
        self.activate()

    # Functie voor het activeren van een event
    def activate(self):
        # Kies een random event uit de events array en roep die functie aan.
        event = self.events[random.randint(0,self.events.__len__()-1)](self)

    # Maak een functie voor elk event
    def loterij(self):
        aantal = 10
        print("Je wint de loterij!")

    def jarig(self):
        aantal = 5
        print("Je bent jarig")

    events = [
        loterij,
        jarig
    ]