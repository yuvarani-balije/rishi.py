import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

# Draw heart with text
for scale in range(11, 17):
    for i in range(120):
        angle = i * (2 * math.pi) / 120

        x = 16 * (math.sin(angle) ** 3)
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )

        t.goto(x * scale, y * scale)
        t.write(
            "rishi",

            align="center",
            font=("Arial", 8, "bold")
        )

turtle.done()
