
class LiteralTable:
    def __init__(self):
        self.literalList = []
        self.locationList = []

    def putliteral(self, literal, location):
        self.literalList.add(literal)
        self.location.add(location)

    def modifyliteral(self, literal, newlocation):
        for i in range(len(self.literalList)):
            if self.literalList[i] == literal:
                self.locationList[i] = newlocation

    def search(self, literal):
        for i in range(len(self.literalList)):
            if self.literalList[i] == literal:
                return self.locationList[i]
        return