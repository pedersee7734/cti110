#Erik Pedersen
#CTI-100
#P4HW3-Factorial
#5 March 2018


userInteger = int (input("Please enter a nonnegative number: " ) )

while userInteger <1:
    userInteger = int ( input ("Please enter a positive number:" ) )

factorial = 1

for currentNumber in range(1, userInteger + 1):
    factorial = factorial *currentNumber

print()
print("The factorial of", userInteger, "is", factorial )
