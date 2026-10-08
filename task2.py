import turtle


def koch_curve(t, order, size):
    """Малює криву Коха заданого рівня рекурсії."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_snowflake(order, size=300):
    """Малює сніжинку з трьох кривих Коха."""
    window = turtle.Screen()
    window.title("Сніжинка Коха")
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії (0 або більше): "))

        if order < 0:
            print("Рівень рекурсії має бути 0 або більше")
        else:
            draw_snowflake(order)
    except ValueError:
        print("Введіть ціле число")