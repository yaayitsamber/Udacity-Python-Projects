import turtle

def draw_triangle(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.left(120)
##        
##def sierpinksi(some_turtle, size, n):
##    if size <= 0:
##        draw_triangle(loca, 100)
##    else: sierpinski(loca, 100, 3)
def dance_turtle():
         #BG COLOR
    window = turtle.Screen()
    window.bgcolor("white")
    loca = turtle.Turtle()
    loca.shape("arrow")
    loca.color("magenta")
    loca.speed(4)
    for i in range(1, 30):
        draw_triangle(loca)
        loca.right(20)
    
    window.exitonclick()


dance_turtle()
