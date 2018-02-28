#Erik Pedersen
#CTI-110
#P4Lab3 Snowflake
#26 Feb 2018



import turtle
t = turtle.Turtle()
t.color("blue")

for i in range (10):
    for i in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.right(36)

