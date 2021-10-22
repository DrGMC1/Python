# Turtle graphics functions
import turtle

# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling

# The circle function draws a circle. The x and y parameters
# are the coordinates of the center point. The radius
# parameter is the circle's radius. The color parameter
# is the fill color, as a string.

def circle(x, y, radius, color):
    turtle.penup()             # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.fillcolor(color)    # Set the fill color
    turtle.pendown()           # Lower the pen
    turtle.begin_fill()        # Start filling
    turtle.circle(radius)      # Draw a circle
    turtle.end_fill()          # End filling

# The line function draws a line from (startX, startY)
# to (endX, endY). The color parameter is the line's color.

def line(startX, startY, endX, endY, color):
    turtle.penup()              # Raise the pen
    turtle.goto(startX, startY) # Move to the starting point
    turtle.pendown()            # Lower the pen
    turtle.pencolor(color)      # Set the pen color
    turtle.goto(endX, endY)     # Draw a square

    
