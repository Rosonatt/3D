import turtle

screen = turtle.Screen()
screen.bgcolor("white")

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)

def draw_spiral():
    colors = ["red", "blue", "green", "orange", "purple", "yellow"]
    for i in range(360):
        spiral_turtle.pencolor(colors[i % 6])
        spiral_turtle.width(i // 100 + 1)
        spiral_turtle.forward(i)
        spiral_turtle.left(59)

draw_spiral()

spiral_turtle.hideturtle()
screen.mainloop()
