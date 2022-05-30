# Deze file is om backend dingen te testen (zonder processing)
# In deze file zal ik ook het een en ander uitleggen over de code.

# Import classes van andere bestanden
import spelers as Spelers
import gebouwen

# Maak $aantal$ spelers aan
spelers = []
for i in range(0,2):
    # Voeg een speler object toe uit het 'spelers' bestand
    spelers.insert(i, Spelers.Speler())



