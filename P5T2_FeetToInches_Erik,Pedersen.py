#Erik Pedersen
#CTI-110
#16 April 2018
#P5T2 Feet to Inches


INCHES_PER_FOOT = 12


def main():
    feet =int(input("Enter a number of Feet: "))

    print(feet, "equals", feet_to_inches(feet), "inches.")



def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
