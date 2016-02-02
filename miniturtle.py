import turtle

def draw_squares(some_turtle):
     for i in range(1,5):                
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_triangle(other_turtle):
     for i in range(3):
        other_turtle.forward(100)
        other_turtle.left(120)
    
def draw_shapes():
    #BG COLOR
    window = turtle.Screen()
    window.bgcolor("white")
##    #TURTLE COLOR
##    brad = turtle.Turtle()
##    brad.shape("turtle")
##    brad.color("pink")
##    brad.speed(6)
##    #GO TURTLE GO
##    for i in range(1,37):
##        draw_squares(brad)
##        brad.right(10)
##   
##    angie = turtle.Turtle()##    angie.shape("arrow")
##    angie.color("purple")
##    angie.circle(100)
##
    arthur = turtle.Turtle()
    arthur.shape("turtle")
    arthur.color("magenta")
    for i in range(1,37):
        draw_triangle(arthur)
        arthur.left(10)
        
        
    window.exitonclick()
    
draw_shapes()
