import turtle

def draw_triangle(some_turtle):
    # some_turtle.fillcolor('blue')
    # some_turtle.begin_fill()
    for i in range(1, 4):
        some_turtle.right(240)
        some_turtle.forward(20)
    some_turtle.end_fill()
    
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    thingy = turtle.Turtle()
    thingy.color('blue')
    thingy.shape('turtle')

    for i in range(1, 14):
        draw_triangle(thingy)
        thingy.right(240)
    
    window.exitonclick()

draw_art()


