import turtle

# Named constants for the triangle's points
TOP_X = 0
TOP_Y = 100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGHT_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')

# The line function draws a line from (startX, startY)
# to (endX, endY). The color parameter is the line's color.

def line(startX, startY, endX, endY, color):
    turtle.penup()              # Raise the pen
    turtle.goto(startX, startY) # Move to the starting point
    turtle.pendown()            # Lower the pen
    turtle.pencolor(color)      # Set the pen color
    turtle.goto(endX, endY)     # Draw a square

# Call the main function.
main()
