import turtle
screen = turtle.Screen()
screen.setup(1600, 1600, startx=200, starty=50)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a +=3
    b +=1
    if b == 210:
        break
    t.hideturtle()

turtle.done()