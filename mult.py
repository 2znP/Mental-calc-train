import random

def rangesMult():
        print("Ok, so whats the minimum value of the numbers?")
        minimumRange=int(input(":"))
        print("Ok, so whats the maximum value of the numbers?\n")
        maximumRange=int(input(":"))

        def multProcess():
            numOne = random.randint(minimumRange, maximumRange)
            numTwo = random.randint(minimumRange, maximumRange)
            print(numOne, "x", numTwo)
            sumOfTwoNumbers=numOne*numTwo
            insertedResult=int(input(":"))
            if insertedResult == sumOfTwoNumbers:
                print("You Are right ):\n")
            else:
                print("No ): it was:", sumOfTwoNumbers,"\n")
            multProcess()
        multProcess()

