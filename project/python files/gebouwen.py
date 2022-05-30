# In deze file staan alle classes van de gebouwen.
# Alle gebouwen hebben bepaalde data die ze meteen en altijd mee krijgen. Deze staat in de def __init__().
# Ze bevatten ook functies om data op te halen. Dit is nodig in classes.

# Standard buildings
class Fabriek:
    def __init__(self):
        self.name = 'Fabriek'
        self.kosten = 6
        self.earnings = 4
        self.population = -3
        self.energy = -4
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Huis:
    def __init__(self):
        self.name = 'House'
        self.kosten = 3
        self.earnings = 0
        self.population = 5
        self.energy = -5
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Energiecentrale:
    def __init__(self):
        self.name = 'Energiecentrale'
        self.kosten = 5
        self.earnings = 0
        self.population = -2
        self.energy = 20
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Monument:
    def __init__(self):
        self.name = 'Monument'
        self.kosten = 20
        self.earnings = 0
        self.population = 0
        self.energy = 0
        self.victory_points = 1

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


# Special buildings
class Dam:
    def __init__(self):
        self.name = 'Dam'
        self.kosten = 4
        self.earnings = 0
        self.population = -2
        self.energy = -2
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Politiebureau:
    def __init__(self):
        self.name = 'Politiebureau'
        self.kosten = 4
        self.earnings = 0
        self.population = -2
        self.energy = -2
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Ziekenhuis:
    def __init__(self):
        self.name = 'Ziekenhuis'
        self.kosten = 4
        self.earnings = 0
        self.population = -2
        self.energy = -2
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten


class Brandweerkazerne:
    def __init__(self):
        self.name = 'Brandweerkazerne'
        self.kosten = 4
        self.earnings = 0
        self.population = -2
        self.energy = -2
        self.victory_points = 0

    def getNaam(self):
        return self.name

    def getKosten(self):
        return self.kosten