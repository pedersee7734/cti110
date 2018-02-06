#CTI-110
#P2HW2- tip tax total
#Erik Pedersen
# 5 Feb 2018

foodCost = float( input( " Please enter the cost of the food: " ))

tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

totalCost = foodCost + tipAmount + salesTax

print( "Food Cost: $" + format ( foodCost, ",.2f"), "Tip amount: $" + \
       format( tipAmount, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "Total Cost: $" + format( totalCost, ",.2f"), sep = "\n" ) 
