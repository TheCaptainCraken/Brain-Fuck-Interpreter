import sys
from bfi import *

with open(sys.argv[1], 'r') as f:
    tha_code = f.read()


interpreter = Bfi(tha_code)
interpreter.execute()