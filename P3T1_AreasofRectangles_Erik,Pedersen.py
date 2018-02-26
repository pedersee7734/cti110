#Erik Pedersen
#CTI-110
#2/25/2018
#P3T1_AreasofRectangles_Erik Pedersen

rectangle1Length = float (input("Please enter the length of rectangle 1: "))
rectangle1Width = float (input("Please enter the length of rectangle 1: "))
rectangle2Length = float (input("Please enter the length of rectangle 2: "))
rectangle2Width = float (input("Please enter the length of rectangle 2: "))
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width

if rectangle1Area > rectangle2Area:
    print ("\nRectangle 1 is larger than Ractangle 2" )
elif rectangle2Area > rectangle1Area :
    print ("\nRectangle 2 is larger than Ractangle 1" )
else:
    print("\nThe rectangles are equal")
  
