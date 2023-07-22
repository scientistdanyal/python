import turtle

pak = turtle.Turtle()

# Set up the turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Adjust the window size as needed
screen.title("Pakistan Flag")
pak.speed(1)

# Draw the green field
pak.up()
pak.goto(-100, -100)
pak.down()
pak.begin_fill()
pak.fillcolor('green')
pak.forward(200)
pak.right(90)
pak.forward(70)
pak.right(90)
pak.forward(200)
pak.right(90)
pak.forward(70)
pak.end_fill()

# Draw the white crescent
pak.up()
pak.goto(-70, 30)
pak.down()
pak.fillcolor('white')
pak.begin_fill()
pak.circle(50, 180)
pak.end_fill()

# Draw the white star
pak.up()
pak.goto(5, 45)
pak.down()
pak.begin_fill()
pak.fillcolor('white')
for _ in range(5):
    pak.forward(30)
    pak.right(144)
pak.end_fill()

# Hide the turtle and display the flag
pak.hideturtle()
screen.mainloop()
