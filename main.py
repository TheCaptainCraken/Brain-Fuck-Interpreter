from bfi import *

with open('code.bf', 'r') as f:
    tha_code = f.read()


interpreter = Bfi(tha_code)
interpreter.execute()