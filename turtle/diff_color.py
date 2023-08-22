import turtle
t = turtle.Turtle()



list_color = ['yellow','blue','green','purple','red']


for i in range(100):
    t.color(list_color[i%5])
    t.pensize(i/5+1)
    t.forward(i)
    t.left(59)




t.hideturtle()
turtle.done()