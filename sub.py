import random

def rangesSub():
        print("Ok, so whats the minimum value of the numbers?")
        minimumRange=int(input(":"))
        print("Ok, so whats the maximum value of the numbers?\n")
        maximumRange=int(input(":"))

        def subProcess():
            numOne = random.randint(minimumRange, maximumRange)
            numTwo = random.randint(minimumRange, maximumRange)
            print(numOne, "-", numTwo)
            sumOfTwoNumbers=numOne-numTwo
            insertedResult=int(input(":"))
            if insertedResult == sumOfTwoNumbers:
                print("You Are right ):\n")
            else:
                print("No ): it was:", sumOfTwoNumbers,"\n")
            subProcess()
        subProcess()

