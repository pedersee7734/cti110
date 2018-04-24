#Erik Pedersen
#CTI-110
#P5HW2_Guessing Game
#April 20 2018








import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100)
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int( input( message ) )
    return userNumber


def restart():
    userInput = input( "Would you like to play again Y/N ? " )
    if userInput == "N" :
        return userCongratulated
    elif userInput == "Y" :
        return letsStart
    
    


def checkUserNumber( userNumber, randomNumber):
    if userNumber > randomNumber:
        return "Too High"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

    

def main():
    userCongratulated = True
    restart = True

    while userCongratulated :
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        message = checkUserNumber( userNumber, randomNumber )



    
        while message != "Congratulations!":
            print ( message )
            userNumber = askUserForNumber( "Try Again : " )
            message = checkUserNumber ( userNumber, randomNumber )
            

        print( message )
        userCongratulated = True



main()

