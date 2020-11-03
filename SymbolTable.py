
class SymbolTable:
    def __init__(self):
        self.symbolList = []
        self.locationList = []

    def putsymbol(self, symbol, location):
        self.symbolList.add(symbol)
        self.locationList.add(location)

    def modifysymbol(self, symbol, newlocation):
        for i in range(len(self.symbolList)):
            if self.symbolList[i] == symbol:
                self.locationList[i] = newlocation

    def search(self, symbol):
        for i in range(len(self.symbolList)):
            if self.symbolList[i] == symbol:
                return self.locationList[i]
        return
