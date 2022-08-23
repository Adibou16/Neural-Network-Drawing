# Drawing application

import turtle
import numpy as np

wn = turtle.Screen()
wn.title("Draw")
wn.bgcolor("white")
wn.setup(1200, 800)

area = turtle.Turtle()
area.speed("fastest")
area.color("black")
area.shape("square")
area.turtlesize(40, 40)
area.setpos(-14, -14)

pen = turtle.Turtle()
pen.speed("fastest")
pen.color("green")
pen.shape("square")
pen.showturtle()
pen.penup()

stamp = turtle.Turtle()
stamp.speed("fastest")
stamp.color("gray")
stamp.shape("square")
stamp.hideturtle()
stamp.penup()

clear = turtle.Turtle()
clear.speed("fastest")
clear.color("red")
clear.shape("square")
clear.shapesize(1, 5)
clear.penup()
clear.setpos(450, -350)

array = np.zeros((28, 28))
lst = []

def follow(x, y):
    arrayX = int(pen.xcor() / 28)
    arrayY = int(pen.ycor() / 28)
    if -14 <= arrayX <= 13 and -14 <= arrayY <= 13:
        pen.goto(x, y)
        stamp.goto(arrayX * 28, arrayY * 28)
        id = stamp.stamp()
        lst.append(id)
        array[arrayX + 14, arrayY + 14] = 1

def clear_stamps():
    for i in range(len(lst) // 2):
        stamp.clearstamp(lst[i])

while True:
    clear.onclick(print("clear"))
    pen.ondrag(follow)
    wn.onclick(follow)
    turtle.mainloop()