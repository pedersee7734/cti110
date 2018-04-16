#Erik Pedersen
#CTI-110
#4/16/2018
#P5T1-Kilometer Converter

def askUserForKilometers():
    userKilometers = float( input( "Please enter the distance" + \
                                   " in kilometers: " ) )
    return userKilometers

def convertkilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles =convertkilometersToMiles ( userKilometersTyped )

    #print()

    print ("\n", userKilometersTyped, " kilometers to miles is " , \
           format( convertedMiles, ".2f" ), " miles", sep="")

main()

    
