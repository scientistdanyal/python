import turtle


t = turtle.Turtle()


wn = turtle.Screen()
wn.title('Color full Circles')

def draw_cicle(x,y,color,rad):
    t.goto(x,y)
    t.begin_fill()
    t.down()
    t.fillcolor(color)
    t.color(color,color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()



t.up()
draw_cicle(0,-50,'red',50)
draw_cicle(100,100,'green',50)
draw_cicle(-100,100,'blue',50)
draw_cicle(100,-100,'purple',-50)
draw_cicle(-100,-100,'yellow',-50)

t.hideturtle()
turtle.done()