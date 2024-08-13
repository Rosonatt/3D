import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flower_turtle = turtle.Turtle()
flower_turtle.speed(0)

def draw_flower():
    colors = ["red", "blue", "green", "orange", "purple", "yellow"]
    for i in range(36):
        flower_turtle.pencolor(colors[i % 6])
        flower_turtle.circle(100)
        flower_turtle.left(10)

draw_flower()


flower_turtle.hideturtle()
screen.mainloop()
