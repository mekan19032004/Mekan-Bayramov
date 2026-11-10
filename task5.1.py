# Name: Mekan Bayramovv
# Date: October 17, 2026
# Description: Draws a colorful house using turtle graphics.

import turtle

artist = turtle.Turtle()
artist.speed(5)
screen = turtle.Screen()
screen.bgcolor("lightblue")


artist.penup()
artist.goto(-100, -100)
artist.pendown()
artist.color("black", "yellow")
artist.begin_fill()

for count in range(4):
    artist.forward(200)
    artist.left(90)

artist.end_fill()

artist.penup()
artist.goto(-120, 100)
artist.pendown()
artist.color("black", "red")
artist.begin_fill()
artist.goto(0, 200)
artist.goto(120, 100)
artist.goto(-120, 100)
artist.end_fill()


artist.penup()
artist.goto(-25, -100)
artist.pendown()
artist.color("black", "brown")
artist.begin_fill()

for count in range(2):
    artist.forward(50)
    artist.left(90)
    artist.forward(80)
    artist.left(90)

artist.end_fill()


artist.penup()
artist.goto(180, 150)
artist.pendown()
artist.color("orange", "yellow")
artist.begin_fill()
artist.circle(35)
artist.end_fill()

artist.hideturtle()
turtle.done()