#Erik Pedersen
#CTI-110
#P4LAB
#11 March 2018




import turtle 

wn = turtle.Screen() 
t = turtle.Turtle() 
 
 
 
 
 
def snowflake(size, pensize, x, y): 
    t.pen(pensize=4) 
    t.penup() 
    t.goto(x, y) 
    t.forward(10*size) 
    t.left(45) 
    t.pendown() 
    t.color("blue") 
 
 
    for i in range(8): 
        branch(size) 
        t.left(45) 
 
 
 
 
 
def branch(size): 
    for i in range(3): 
        for i in range(3): 
            t.forward(10.0*size/3) 
            t.backward(10.0*size/3) 
            t.right(45) 
        t.left(90) 
        t.backward(10.0*size/3) 
        t.left(45) 
    t.right(90) 
    t.forward(10.0*size) 
 
 
snowflake(8, 6, 0, 0)  
 

wn.exitonclick() 
