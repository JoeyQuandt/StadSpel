# Deze file bevat de class en alle nodige data voor de spelers.

import gebouwen


class Speler:
    def __init__(self):
        self.geld = 10
        self.energie = 0
        self.inwoners = 0
        self.gebouwen = [
            gebouwen.Huis(),
            gebouwen.Fabriek(),
            gebouwen.Energiecentrale()
        ]

    def getGeld(self):
        return self.geld

    def getEnergie(self):
        return self.energie

    def getInwoners(self):
        return self.inwoners

    def getGebouwen(self):
        return self.gebouwen