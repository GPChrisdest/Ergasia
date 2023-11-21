import turtle

t = turtle.Turtle()

class Collumn():
    def __init__(self,height,position):
        self.height = height
        self.position = position

def collumn(height,position):
    #canvas 700x650
    t.hideturtle()
    t.speed(200)
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

def swap(c1,c2,l):
    l.insert(c1.position,c2)
    l.insert(c2.position,c1)
    #l.pop(c2.position+1)
    #l.pop(c2.position+2)


l = [5,8,6,10]
n = 0
c = []
for i in l:
    c.append(Collumn(i,n))
    n += 1

for item in c:
    collumn(item.height,item.position)

swap(c[0],c[3],c)

for i in c:
    collumn(i.height,i.position)
turtle.exitonclick()
