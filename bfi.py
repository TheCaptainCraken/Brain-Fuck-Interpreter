class Bfi:
    def __init__(self, code) -> None:
        self.symbols = '><+-.,[]'
        self.brackets = {}
        self.cells = [0 for i in range(30_000_0)]
        self.pointer = 0
        self.code = self.trim(code)
        self.find_loops()
    
    def trim(self, raw) -> str:
        cleaned = ''
        for symbol in raw:
            if(symbol in self.symbols):
                cleaned+=symbol
        return cleaned

    def find_loops(self):
        pc = 0
        code = self.code 
        for i in range(len(self.code)):
            if(self.code[i] == '['):
                pc+=1
        for _ in range(pc):
            pos1 = None
            pos2 = None
            k = 0
            for j in range(len(code)-1, 0, -1):
                if(code[j] == ']' and pos1 == None):
                    pos1 = j
                elif(code[j] == ']'):
                    k+=1
                elif(code[j] == '['):
                    if(k == 0):
                        pos2 = j
                    else:
                        k-=1
            code = code[:pos1] + '#' + code[pos1+1:]
            code = code[:pos2] + '#' + code[pos2+1:]
            self.brackets[pos1] = pos2
                
    def op(self, o, a):
        match o:
            case '>':
                self.pointer+=1
            case '<':
                self.pointer-=1
                if(self.pointer < 0):
                    raise IndexError('The pointer is at position {0}'.format(self.pointer))
            case '+':
                self.cells[self.pointer]+=1
            case '-':
                self.cells[self.pointer]-=1
            case '.':
                print(chr(self.cells[self.pointer]), end='')
            case ',':
                try:
                    self.cells[self.pointer] = ord(input('=> '))
                except TypeError:
                    raise TypeError('You inserted more than one character >:(')
            case ']':
                if(self.cells[self.pointer] != 0):
                    a = self.brackets[a]
            case '[':
                if(self.cells[self.pointer] == 0):
                    a = list(self.brackets.keys())[list(self.brackets.values()).index(a)]
            case _:
                pass
        return a
    def execute(self):
        pos = 0
        while pos < len(self.code):
            pos = self.op(self.code[pos], pos)
            pos+=1

    def __str__(self) -> str:
        return self.code