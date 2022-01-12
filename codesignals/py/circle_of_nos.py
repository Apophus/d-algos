def circleOfNumbers(n, firstNumber):
    return int(n/2 + firstNumber)%n

print(circleOfNumbers(10, 2))