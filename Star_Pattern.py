import turtle

screen = turtle.Screen()
screen.bgcolor("black")

star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.color("yellow")

def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
        star_turtle.forward(size)
        star_turtle.left(72)

for _ in range(50):
    star_turtle.penup()
    x = turtle.randint(-200, 200)
    y = turtle.randint(-200, 200)
    star_turtle.goto(x, y)
    star_turtle.pendown()
    draw_star(turtle.randint(10, 50))

star_turtle.hideturtle()
screen.mainloop()
