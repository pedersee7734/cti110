#Erik Pedersen
#CTI-110
#P3HW1-Age Classifier
#2/25/2018

personsAge = int( input ("Enter the persons age in years: "))

if personsAge <= 1:
    print ("\nThe person is an infant")
elif personsAge < 13:
    print ("\nThe person is a child")
elif personsAge < 20:
    print ("\nThe person is a teenager")
elif personsAge >= 20:
    print ("\nThe person is an adult")
