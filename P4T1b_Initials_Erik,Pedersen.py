#Erik Pedersen
#CTI-110
#P4T1B- Initials
#3 Mar 2018



import turtle             
win = turtle.Screen()      
e = turtle.Turtle()


e.pensize(4)        
e.pencolor("blue")     
e.shape("turtle")

#setting new start location
e.penup()
e.goto(-200,200)
e.pendown()


#First Letter

e.forward(200)
e.back(200)
e.right(90)
e.forward(250)
e.right(180)
e.forward(125)
e.right(90)
e.forward(150)
e.back(150)
e.right(90)
e.forward(150)
e.left(90)
e.forward(200)

#last letter starts
e.penup()
e.forward(150)
e.left(90)
e.pendown()
e.forward(275)
e.right(90)
e.forward(175)
e.right(90)
e.forward(150)
e.right(90)
e.forward(175)
