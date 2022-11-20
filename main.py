from sum import *
from sub import *
from mult import *
import random

minimumRange = 0

def menu():
    print("Hello, what you want to train?\n\n1. -Sum\n2. -Multiplication\n3. -Subtraction\n") 
    responseOne = int(input(":"))
    if responseOne==1:
        rangesSum()
    elif responseOne==2:
        rangesMult()
    elif responseOne==3:
        rangesSub()
menu()

    