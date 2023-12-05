import turtle
import colorsys

def draw_spiral():
    tortuga = turtle.Turtle()
    ventana = turtle.Screen()
    ventana.bgcolor("black")
    tortuga.speed(0)

    for i in range(125):
        hue = i / 125.0
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        tortuga.pencolor(color)
        tortuga.forward(i * 2)
        tortuga.right(120)

    ventana.exitonclick()

if __name__ == "__main__":
    draw_spiral()
