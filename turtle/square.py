import turtle


mark = turtle.Turtle() # to create turtle
mark.setheading(60)
mark.begin_fill()
mark.fillcolor('blue')
mark.speed(1)
mark.color('blue','red')
mark.fillcolor('blue')

wn = turtle.Screen() 
# wn.colormode(255) #use this for RGB color
wn.bgcolor('black')
wn.title('My turtle app')


for i in range(4):
    mark.forward(100)
    mark.left(90)


mark.end_fill()
mark.hideturtle()

turtle.done()




