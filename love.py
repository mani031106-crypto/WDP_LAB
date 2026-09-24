import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.title("I Love You ❤️")
screen.bgcolor("black")
screen.setup(width=800, height=700)

# Turtle setup
t = turtle.Turtle()
t.speed(0)  # Fast drawing
t.hideturtle()
t.penup()
t.color("#ffb6c1")

# Draw text in heart shape
for scale in range(11, 17):
    for i in range(120):
        angle = i * 2 * math.pi / 120

        x = 16 * (math.sin(angle) ** 3) * scale

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        t.goto(x, y)

        t.write(
            "I love you",
            align="center",
            font=("Arial", 8, "bold")
        )

# Keep window open
turtle.done()