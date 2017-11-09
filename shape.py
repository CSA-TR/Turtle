import turtle
wn=turtle.Screen()
wn.bgcolor("black")

jaja=turtle.Turtle()
jaja.color("white")
jaja.pensize(.1)
jaja.shape("turtle")
jaja.shapesize(5)

jaja.up()
jaja.forward(100)
jaja.down()

for i in range(100):
    jaja.speed(1000000000)
    jaja.forward(100)
    jaja.left(200)
    jaja.right(3.5)
    jaja.right(4.4)

    jaja.forward(175)
    jaja.left(120)

import turtle

jajaxd=turtle.Turtle()
jajaxd.color("white")
jajaxd.pensize(.1)
jajaxd.shape("turtle")
jajaxd.penup()

for size in range(10):
    jajaxd.forward(50)
    jajaxd.stamp()
    jajaxd.forward(-50)
    jajaxd.right(36)
    wn.exitonclick()

    

