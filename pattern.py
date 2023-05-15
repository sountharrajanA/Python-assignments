import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the background color
turtle.bgcolor('black')

# Set the turtle shape and color
my_turtle.shape('turtle')
my_turtle.color('white')

# Draw the pattern
for i in range(36):
    my_turtle.circle(100)  # Draw a circle with radius 100
    my_turtle.right(10)  # Turn right by 10 degrees

# Hide the turtle
my_turtle.hideturtle()

# Close the turtle graphics window
turtle.done()
