#Erik Pedersen
#CTI-110
#4/17/2018
#P5HW1 Test Average and Grades


def calc_average( score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5 ) /5
    return average



def determine_grade( userScore ):
    if( userScore <60 ):
        return "F"
    elif( userScore <70 ):
        return "D"
    elif( userScore <80 ):
        return "C"
    elif( userScore <90 ):
        return "B"
    elif( userScore <101 ):
        return "A"

def askForScores():
    score1 = float( input( "Please enter test grade 1: " ))
    score2 = float( input( "Please enter test grade 2: " ))
    score3 = float( input( "Please enter test grade 3: " ))
    score4 = float( input( "Please enter test grade 4: " ))
    score5 = float( input( "Please enter test grade 5: " ))

    return score1, score2, score3, score4, score5

def printTableOfResults( score1, score2, score3, score4, score5, ):
    print( "Score\tLetter Grade" )
    print( str( score1 ) + "\t\t" + determine_grade( score1 ), \
           str( score2 ) + "\t\t" + determine_grade( score2 ), \
           str( score3 ) + "\t\t" + determine_grade( score3 ), \
           str( score4 ) + "\t\t" + determine_grade( score4 ), \
           str( score5 ) + "\t\t" + determine_grade( score5 ), sep = "\n" )
    print()
    print( "Your average test score is:", calc_average( score1, score2, score3, score4, score5 )) 


def main():
    score1, score2, score3, score4, score5 = askForScores()
    print()
    printTableOfResults( score1, score2, score3, score4, score5 )

main()
