import turtle

## set up the turtle screen size and draw window
window_width = 600
window_height = 300
screen = turtle.Screen()
screen.setup(window_width, window_height, startx=0, starty=0)

## create the turtle object
my_turtle = turtle.Turtle()

## draw the German flag
my_turtle.speed('fastest')
my_turtle.width(12)
my_turtle.pensize(3)

my_turtle.color('black')
my_turtle.goto(-100, 200)
my_turtle.pendown()
my_turtle.forward(30)
my_turtle.penup()

my_turtle.color('yellow')
my_turtle.goto(-160, 200)
my_turtle.pendown()
my_turtle.forward(30)
my_turtle.penup()

my_turtle.color('red')
my_turtle.goto(-220, 200)
my_turtle.pendown()
my_turtle.forward(30)
my_turtle.penup()

my_turtle.speed(0)
screen.exitonclick()
