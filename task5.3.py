# Name: Mekan bayramov
# Date: October 17, 2026
# Description: Draws and fills a regular polygon.

import turtle

sides = int(input("Enter the number of sides (3 or more): "))
length = float(input("Enter the side length: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

if sides < 3 or length <= 0:
    print("Please enter at least 3 sides and a positive length.")
else:
    artist = turtle.Turtle()
    artist.color(line_color, fill_color)

    artist.begin_fill()

    for count in range(sides):
        artist.forward(length)
        artist.left(360 / sides)

    artist.end_fill()
    turtle.done()