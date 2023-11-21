import turtle as t

def collumn(height,position):
    #canvas 700x650
    t.penup()
    if position < 35:
        position = -700 + 31*position
    else:
        position = 700 - 31*position
    t.goto(position,0)

    draw(height)

def draw(height):
    t.begin_fill()
    t.fillcolor('blue')
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(10*height)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10*height)
    t.left(90)
    t.end_fill()