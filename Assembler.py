from InstTable import InstTable
from SymbolTable import SymbolTable
from LiteralTable import LiteralTable
from TokenTable import TokenTable
from TokenTable import Token


class Assembler:
    def __init__(self, instfile):
        self.lineList = []
        self.symtabList = []
        self.literaltabList = []
        self.TokenList = []
        self.codeList = []
        self.instTable = InstTable(instfile)

    def inputfile(self, filename):
        file = open(filename, 'r')
        while file.readline() != -1:
            if file.readline()[0] == '.':
                continue
            self.lineList.add(file.readline())
        file.close()

    def pass1(self):
        #k = 0
        #loc = 0
        size = len(self.lineList)
        for i in range(size):
            self.symtabList.add(SymbolTable())
            self.literaltabList.add(LiteralTable())
         #   tmp = None
           # while (True):
          #      tmp = Token(self.lineList[i])

    def printsymboltable(self, filename):
        file = open(filename, 'w')
        for i in range(len(self.symtabList)):
            for j in range(len(self.symtabList[i].symbolList)):
                line = self.symtabList[i].symbolList[j] + self.symtabList[i].locationList[j]
                file.write(line)
        file.close()

    def printliteraltable(self, filename):
        file = open(filename, 'w')
        for i in range(len(self.literaltabList)):
            for j in range(len(self.literaltabList[i].literalList)):
                line = self.literaltabList[i].literalList[j] + self.literaltabList[i].locationList[j]
                file.write(line)
        file.close()

    def pass2(self):
        return

    @staticmethod
    def printcode(filename):
        file = open(filename, 'w')
        file.close()

    def __main__(self):
        self.assembler = Assembler("inst.txt")
        self.inputfile("input.txt")
        self.pass1()
        self.printsymboltable("symtab_20150234")
        self.printliteraltable("literaltab_20150234")
        self.pass2()
        self.printcode("output_20150234")
