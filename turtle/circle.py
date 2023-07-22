import turtle


c = turtle.Turtle()
c.shape('arrow')
c.speed(1)
c.begin_fill()
c.fillcolor('yellow')
c.color('yellow')
c.setheading(360)


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('to draw circle')

c.forward(100)
# c.circle(100) #to draw circle
# c.circle(100,steps=3) #to dran triangle
c.circle(100,steps=3)

c.end_fill()
c.hideturtle()
turtle.done()