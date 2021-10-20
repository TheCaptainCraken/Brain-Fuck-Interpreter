import sys
from bfi import *

#try open a file
try:
    with open(sys.argv[1], 'r') as f:
        tha_code = f.read()
except FileNotFoundError:
    print('Use a valid path not "{0}"! >:/'.format(sys.argv[1]))
    sys.exit()

#create an interpreter to then execute the code
interpreter = Bfi(tha_code)
interpreter.execute()