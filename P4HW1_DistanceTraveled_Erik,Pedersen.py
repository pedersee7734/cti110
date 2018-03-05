#Erik Pedersen
#CTI-110
#P4HW1 Distance Traveled
#5 Mar 2018

start = "\033[1m" #this is what i found to make bold text, but i couldnt figure out how to add it to the user entry
end = "\033[0;0m"

vehicleSpeed = float( input( "What is the speed of the vehicle in MPH:" ) )
timeTraveled = int( input( "How many hours has it traveled?: " ) )

print()

print ("\nHour","\tDistance Traveled" )
print()
print ("-------------------------")
print()
for currentHour in range ( 1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour, "\t", distanceTraveled)
