
class TokenTable:
    def __init__(self, symTable, literalTable, instTable):
        self.MAX_OPERAND = 3
        self.nFlag = 32
        self.iFlag = 16
        self.xFlag = 8
        self.bFlag = 4
        self.pFlag = 2
        self.eFlag = 1
        self.symTab = None
        self.literalTab = None
        self.instTab = None
        self.tokenList = None
        self.instTab = instTable
        self.symTab = symTable
        self.literalTab = literalTable

    def puttoken(self, line):
        self.tokenList.add(Token(line))
        if (self.tokenList[-1].operator == "LTORG") or (self.tokenList[-1].operator == "END"):
            newlocation = self.tokenList[len(self.tokenList) - 2].location
            l = True
            for i in range(len(self.tokenList)):
                if self.tokenList[i].operand is None:
                    continue
                elif self.tokenList[i].operand[0][0] == '=':
                    for j in range(len(self.literalTab.literalList)):
                        if self.literalTab.literalList[j] == self.tokenList[i].operand[0] and (not self.literalTab.locationList[j] == self.tokenList.operand[0]):
                            l = False
                            break
                    if l:
                        if len(self.literalTab.literalList) != 0 :
                            tokenb = self.tokenList.gettoken(len(self.tokenList) - 2)
                            if tokenb.operator == "WORD":
                                newlocation += 3
                            elif tokenb.operator == "BYTE":
                                newlocation += int((len(tokenb.operand[0]) - 3 )/ 2)
                            elif tokenb.operator == "RESW":
                                newlocation += int(tokenb.operand[0]) * 3
                            elif tokenb.operator == "RESB":
                                newlocation += int(tokenb.operand[0])
                            elif self.instTab.search(tokenb.operator):
                                if tokenb.operator[0] == '+':
                                    newlocation += 1
                                    newlocation += 3
                        self.literalTab.modifyliteral(self.tokenList[i].operand[0], newlocation)
                    l = False
            return

        token = self.tokenList.gettoken(-1)
        if len(self.tokenList) > 1:
            tokenb = self.tokenList.gettoken(len(self.tokenList) - 2)
            if tokenb.operator == "LTORG":
                token.location = self.literalTab.locationList[-1]
                str = self.literalTab.literalList[-1]
                if str.slice[0:2] == "=C":
                    token.location += len(str.slice[3:-1])
                else:
                    token.location += int(len(str.slice[3:-1]) / 2)
                if tokenb.operator == "START" or tokenb.operator == "CSECT":
                    token.location += 0
                elif tokenb.operator == "WORD":
                    token.location += tokenb.location + 3
                elif tokenb.operator == "BYTE":
                    token.location += tokenb.location + int((len(tokenb.operand[0]) - 3) / 2)
                elif tokenb.operator == "RESW":
                    token.location += tokenb.location + int(tokenb.operand[0]) * 3
                elif tokenb.operator == "RSWB":
                    token.location += tokenb.location + int(tokenb.operand[0])
                elif self.instTab.search(tokenb.operator):
                    if tokenb.operator[0] == '+':
                        token.location += 1
                    token.location += tokenb.location + self.instTab.getformat(tokenb.operator)
                else:
                    token.location += tokenb.location

                if token.operator == "EQU":
                    if not token.oprand[0] == '*':
                        if token.oprand[1] == '+':
                            token.location = self.symTab.search(token.oprand[0]) + self.symTab.search(token.oprand[2])
                        elif token.oprand[1] == '-':
                            token.location = self.symTab.search(token.oprand[0]) - self.symTab.search(token.oprand[2])
                        elif token.oprand[1] == '*':
                            token.location = self.symTab.search(token.oprand[0]) * self.symTab.search(token.oprand[2])
                        elif token.oprand[1] == '/':
                            token.location = self.symTab.search(token.oprand[0]) / self.symTab.search(token.oprand[2])
            else:
                token.location = 0

            if not token.label == "\t":
                self.symTab.modifysymbol(token.label, token.location)

    def gettoken(self, index):
        return self.tokenList[index]

    def makeobjectcode(self, index):
        tmp = self.gettoken(index)

    def getobjectcode(self, index):
        return self.tokenList[index].objectCode


class Token:
    def __init__(self, line):
        self.location = 0
        self.label = ""
        self.operator = ""
        self.operand = []
        self.commet = None
        self.nixbpe = None
        self.objectCode = ""
        self.byteSize = None
        self.parsing(line)

    def parsing(self, line):
        str = line.split('\t')
        self.label = str[0]
        self.operator = str[1]
        self.comment = str[3]
        if str[2] != '\t':
            op = str[2].split(",")
            for i in range(len(op)):
                self.operand[i] = (op[i])

        if "EQU" == self.operator or "WORD" == self.operator:
            if "*" == self.operand[0]:
                return
            ch = None
            ca = False
            for i in range(len(self.operand[0])):
                ch = self.operand[i]
                if ch == '+' or ch == '-' or ch == '*' or ch == '/':
                    ca = True
                    break
            if ca:
                op = self.operand[0].split(ch)
                self.operand[0] = (op[0])
                self.operand[1] = ch
                self.operand[2] = (op[1])

    def setflag(self, flags):
        self.nixbpe += flags

    def getflag(self, flags):
        return self.nixbpe & flags

