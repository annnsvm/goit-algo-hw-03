import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)

def draw_koch_snowflake(order, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.penup()
    fractal_turtle.goto(-size / 2, -size / 2 / 3 ** 0.5)
    fractal_turtle.pendown()

    for _ in range(3):
        koch_snowflake(fractal_turtle, order, size)
        fractal_turtle.right(120)

    screen.mainloop()

if __name__ == "__main__":
    order = int(input("Enter the order of the Koch Snowflake: "))
    size = int(input("Enter the size of the Koch Snowflake: "))

    draw_koch_snowflake(order, size)