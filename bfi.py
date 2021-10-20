class Bfi:
    def __init__(self, code) -> None:
        self.__symbols = '><+-.,[]'                                    #everything else is a comment
        self.__brackets = {}                                           #position of [] in code to do loops
        self.__cells = [0 for i in range(30_000_0)]                    #initialize the memory and the pointer
        self.__pointer = 0
        self.__code = self.__trim(code)                                #eliminate comments from code
        self.__find_loops()                                            #find all the [] and save their position
    
    #returns only the code from a file
    def __trim(self, raw_code) -> str:
        clean_code = ''
        for symbol in raw_code:
            if(symbol in self.__symbols):
                clean_code+=symbol
        return clean_code

    #finds [] in the code and then saves their position in self.__brackets to
    #do loops in runtime
    def __find_loops(self):
        loops = 0
        code = self.__code 
        for i in range(len(self.__code)):
                loops = loops + 1 if self.__code[i] == '[' else loops
        for _ in range(loops):
            end_loop = None
            start_loop = None
            ignore = 0
            for i in range(len(code)-1, 0, -1):
                if(code[i] == ']' and end_loop == None):
                    end_loop = i
                elif(code[i] == ']'):
                    ignore+=1
                elif(code[i] == '['):
                    if(ignore == 0):
                        start_loop = i
                    else:
                        ignore-=1
            code = code[:end_loop] + '#' + code[end_loop+1:]
            code = code[:start_loop] + '#' + code[start_loop+1:]
            self.__brackets[end_loop] = start_loop
    
    #takes a symbol and the code_pointer to then execute the corresponding instruction_
    #   >   move the memory pointer right
    #   <   move the memory pointer left
    #   +   increment the number in the memory cell pointed by the memory pointer
    #   -   decrement the number in the memory cell pointed by the memory pointer
    #   .   output the ascii char in the memory cell pointed by the memory pointer
    #   ,   intput a single char in the memory cell pointed by the memory pointer
    #   [   jump to the corresponding ] if the memory cell pointed by the memory pointer is 0
    #   ]   jump to the corresponding [ if the memory cell pointed by the memory pointer is NOT 0
    def __op(self, op, code_pointer):
        match op:
            case '>':
                self.__pointer+=1
            case '<':
                self.__pointer-=1
                if(self.__pointer < 0):
                    raise IndexError('The pointer is at position {0}'.format(self.__pointer))
            case '+':
                self.__cells[self.__pointer]+=1
            case '-':
                self.__cells[self.__pointer]-=1
            case '.':
                print(chr(self.__cells[self.__pointer]), end='')
            case ',':
                try:
                    self.__cells[self.__pointer] = ord(input('=> '))
                except TypeError:
                    raise TypeError('You inserted more than one character >:(')
            case ']':
                if(self.__cells[self.__pointer] != 0):
                    code_pointer = self.__brackets[code_pointer]
            case '[':
                if(self.__cells[self.__pointer] == 0):
                    code_pointer = list(self.__brackets.keys())[list(self.__brackets.values()).index(code_pointer)]
            case _:
                pass
        return code_pointer
    
    #run the program starting from the first symbol and end it after the last one :)
    def execute(self):
        pos = 0
        while pos < len(self.__code):
            pos = self.__op(self.__code[pos], pos)
            pos+=1

    def __str__(self) -> str:
        return self.__code