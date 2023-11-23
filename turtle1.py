import turtle

t = turtle.Turtle()
t.pencolor('white')

class Collumn():
    def __init__(self,height,position):
        self.height = height
        self.position = position

def create(height,position,color='blue'):
    #canvas 700x650
    t.hideturtle()
    t.speed('fastest')
    t.penup()
    if position < 35:
        position = -700 + 31*position
    else:
        position = 700 - 31*position
    t.goto(position,0)
    draw(height,color)

def draw(height,color):
    t.begin_fill()
    t.fillcolor('blue')
    t.fillcolor(color)
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
    t.penup()

def swap(c1,c2):
    create(c1.height,c1.position,'white')
    create(c2.height,c1.position)
    create(c1.height,c2.position)

l = [5,8,6,30,10,25,17,23,15,9]
n = 0
c = []
for i in l:
    c.append(Collumn(i,n))
    n += 1
for item in c:
    create(item.height,item.position)

swap(c[3],c[4])

turtle.exitonclick()