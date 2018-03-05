#Erik Pedersen
#CTI-110
#P4HW2-Running Total
#5 March 2018


total = 0
userNumber = float( input( "Enter a number:"))


while userNumber > -1:
    total = total + userNumber
    print()
    userNumber = float( input ("Enter a number:"))

print()
print ("Total:",total)




