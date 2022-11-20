import random

def rangesSum():
        print("Ok, so whats the minimum value of the numbers?")
        minimumRange=int(input(":"))
        print("Ok, so whats the maximum value of the numbers?")
        maximumRange=int(input(":"))

        def sumProcess():
            numOne = random.randint(minimumRange, maximumRange)
            numTwo = random.randint(minimumRange, maximumRange)
            print(numOne, "+", numTwo)
            sumOfTwoNumbers=numOne+numTwo
            insertedResult=int(input(":"))
            if insertedResult == sumOfTwoNumbers:
                print("You Are right")
            else:
                print("No ): it was:", sumOfTwoNumbers)
            sumProcess()
        sumProcess()
