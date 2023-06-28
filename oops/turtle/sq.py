import turtle
wn = turtle.Screen()

wn.bgcolor('light green')


alex = turtle.Turtle()
alex.width(3)
alex.speed(0)



total = 100

while total !=0:
    for i in range(4):
        alex.forward(total)
        alex.left(90)
    total = total - 10
alex.left(45)
alex.forward(100)

turtle.exitonclick()