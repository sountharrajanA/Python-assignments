import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()

# Draw your custom object
for _ in range(8):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(45)  # Turn right by 45 degrees

# Hide the turtle
my_turtle.hideturtle()

# Close the turtle graphics window
turtle.done()
