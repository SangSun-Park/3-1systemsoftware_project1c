
class InstTable:
    def __init__(self, filename):
        self.inst = {}
        self.openfile(filename)

    def openfile(self, filename):
        file = open(filename, 'r')
        while file.readline() != -1:
            ins = Instruction(file.readline())
            self.inst[ins['name']] = ins
        file.close()

    def getname(self, name):
        if name[0] == '+':
            name += 1
        return self.inst['name']

    def getformat(self, name):
        if name[0] == '+':
            name += 1
        return self.inst['name']['format']

    def getopcode(self, name):
        if name[0] == '+':
            name += 1
        return self.inst['name']['opcode']

    def getopnum(self, name):
        if name[0] == '+':
            name += 1
        return self.inst['name']['opnum']

    def search(self, name):
        if name[0] == '+':
            name += 1
        if 'name' in self.inst:
            return True
        else:
            return False

class Instruction:
    def __init__(self, line):
        self.name = ""
        self.format = 0
        self.opcode = ""
        self.opnum = 0
        self.parsing(line)

    def parsing(self, line):
        str = line.split('\t')
        self.name = str[0]
        self.format = int(str[1])
        self.opcode = str[2]
        self.opnum = int(str[3])