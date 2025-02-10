import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Smiling Face using Python")
screen.setup(width=600, height=600)

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the turtle speed to the fastest

# Draw the face
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)

# Draw the eyes
t.penup()
t.goto(-100, 50)
t.pendown()
t.dot(40)
t.penup()
t.goto(100, 50)
t.pendown()
t.dot(40)

# Draw the mouth
t.penup()
t.goto(-100, -70)
t.pendown()
t.setheading(-60)
t.circle(100, 120)

# Hide the turtle and display the result
t.hideturtle()
input()
