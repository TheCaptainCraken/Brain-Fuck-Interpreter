class Bfi:
    def __init__(self, code) -> None:
        self.symbols = '><+-.,[]'
        self.cells = [0 for i in range(30_000)]
        self.pointer = 0
        self.code = self.trim_that_bitch(code)
    
    def trim_that_bitch(self, the_bich) -> str:
        trimmed_bitch = ''
        for symbol in the_bich:
            if(symbol in self.symbols):
                trimmed_bitch+=symbol
        return trimmed_bitch

    def op(self, o):
        match o:
            case '>':
                self.pointer+=1
            case '<':
                self.pointer-=1
            case '+':
                self.cells[self.pointer]+=1
            case '-':
                self.cells[self.pointer]+=1
            case '.':
                print(chr(self.cells[self.pointer]), end='')
            case ',':
                self.cells[self.pointer] = input('=> ')
            case _:
                pass
    def execute(self):
        pos = 0
        while pos < len(self.code):
            pass

    def __str__(self) -> str:
        return self.code