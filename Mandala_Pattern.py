import turtle

screen = turtle.Screen()
screen.bgcolor("white")

mandala_turtle = turtle.Turtle()
mandala_turtle.speed(0)

def draw_mandala():
    colors = ["red", "blue", "green", "orange", "purple", "yellow"]
    for i in range(60):
        mandala_turtle.pencolor(colors[i % 6])
        mandala_turtle.circle(100)
        mandala_turtle.left(6)
        for j in range(4):
            mandala_turtle.forward(100)
            mandala_turtle.right(90)
            mandala_turtle.forward(100)
            mandala_turtle.right(90)
            mandala_turtle.forward(100)
            mandala_turtle.right(90)
            mandala_turtle.forward(100)
            mandala_turtle.right(90)
        mandala_turtle.right(6)

draw_mandala()

mandala_turtle.hideturtle()
screen.mainloop()
