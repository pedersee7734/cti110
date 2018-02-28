#Erik Pedersen
#CTI-110
#P4T2 Bug Collector
#28 Feb 2018




totalDays = 7
totalNumberOfbugs = 0

for currentDay in range( 1, totalDays + 1 ):
    bugsCollected = int ( input( "How many bugs were collected on day " + \
                                 str( currentDay ) + ":" ) )
    totalNumberOfbugs += bugsCollected
print()
print("The total number of bugs collected for all", totalDays, "days is" , \
      totalNumberOfbugs)
