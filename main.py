import sys
from bfi import *

try:
    with open(sys.argv[1], 'r') as f:
        tha_code = f.read()
except FileNotFoundError:
    print('Asshole next time use a valid path not "{0}"! >:/'.format(sys.argv[1]))
    sys.exit()


interpreter = Bfi(tha_code)
interpreter.execute()