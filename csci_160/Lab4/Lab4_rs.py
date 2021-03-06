"""
Author: Rand Seay
Objective: Working with loops (Time for some fun)
"""

from math import factorial

def sectionIntro(nameOfSection):
    """
    Output a section header based on a passed in name
    """
    print()
    print("="*80)
    print("Welcome to", nameOfSection)
    print("="*80)
    print()

def getIntFromUser(prompt):
    """
    Return a positive integer based on user input and a passed-in prompt
    """
    while True:
        try:
            userInput = int(input(prompt + "\n> "))

            if userInput > 0:
                break
            else:
                userInput = "Please provide a positive whole number as a value."
        except ValueError:
            userInput = "Please provide a positive whole number as a value"
    return userInput

# Part 1: Summation

sectionIntro("Summation")

numToSum = getIntFromUser("Please provide a positive whole number to be summed.")
print()

yourSum = 0
for num in range(1, numToSum + 1):
    yourSum += num

    print(num, end=" ")
    if num < numToSum:
        print("+", end=" ")
    else:
        print("=", yourSum)

print("The sum for all of the numbers from 1 to {} is {}".format(numToSum, yourSum))

# Part 2: Factorial

sectionIntro("Factorial")

numToGetFactorial = getIntFromUser("Please provide a positive whole number to get the factorial of.")
print()

yourFactorial = 1
for num in range(1, numToGetFactorial + 1):
    yourFactorial *= num

    print(num, end=" ")
    if num < numToGetFactorial:
        print("*", end=" ")
    else:
        print("=", yourFactorial)

print("The factorial of {} is {}".format(numToGetFactorial, yourFactorial))

# Part 3: Approximate e

sectionIntro("Approximate e")

iterationsOfE = getIntFromUser("Please provide a positive whole number to determine the number of iterations\nused in the approximation of e.")
print()

approxOfE = 1
print("1 +", end=" ")
for num in range(1, iterationsOfE + 1):
    approxOfE += 1 / factorial(num)

    print("(1/{}!)".format(num), end=" ")
    if num < iterationsOfE:
        print("+", end=" ")
    else:
        print("=", approxOfE)

print("The approximation of e after {} iterations is {}".format(iterationsOfE, approxOfE))

# Part 4: Approximate Pi

sectionIntro("Approximate Pi")

iterationsOfPi = getIntFromUser("Please provide a positive whole number to determine the number of iterations\nused in the approximation of Pi.")
print()

approxOfPi, sign = 0, 1
print(approxOfPi, end=" ")
for num in range(1, iterationsOfPi * 2 + 1, 2):
    approxOfPi += sign * (4 / num)

    if num < iterationsOfPi * 2:
        print("+ {}*(4/{})".format(sign, num), end=" ")
    else:
        print("=", approxOfPi)

    sign = -sign

print("=", approxOfPi)
print("The approximation of Pi after {} iterations is {}".format(iterationsOfPi, approxOfPi))

# Part 5: Draw a Triangle

sectionIntro("Draw a Triangle.")

triangleSide = getIntFromUser("Please provide positive whole number for the side length of the triangle.")
print()

for num in range(1, triangleSide + 1):
    print("*"*num)
