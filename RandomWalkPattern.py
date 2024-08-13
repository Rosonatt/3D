import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

walk_turtle = turtle.Turtle()
walk_turtle.speed(0)
walk_turtle.width(2)

def random_walk(steps, step_size):
    colors = ["red", "blue", "green", "orange", "purple", "yellow"]
    for _ in range(steps):
        walk_turtle.pencolor(random.choice(colors))
        angle = random.choice([0, 90, 180, 270])
        walk_turtle.setheading(angle)
        walk_turtle.forward(step_size)

random_walk(200, 20)

walk_turtle.hideturtle()
screen.mainloop()
