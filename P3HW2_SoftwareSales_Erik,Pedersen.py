#Erik Pedersen
#CTI-110
#P3HW2-Software Sales
#2\25\2018



numberOfPackages = int( input ("Please enter the number of packages bought: "))
packagePrice = 99
if numberOfPackages < 10:
    discount = 0;
elif numberOfPackages < 20:
    discount = 0.10
elif numberOfPackages < 50:
    discount = 0.20
elif numberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = numberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print ("\nAmount of Discount : $" + format ( discountAmount, ",.2f" ) + \
       "\nTotal amount: $" + format ( total, ",.2f" ))
