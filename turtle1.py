import turtle as t

t = t.Turtle()


t.pencolor('white')

class Collumn():
    def __init__(self,height,position):
        self.height = height
        self.position = position

def collumn(height,position):
    #canvas 700x650
    t.hideturtle()
    t.speed(200)

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

    draw(height,color='blue')

def draw(height,color='blue'):
    t.begin_fill()
    t.fillcolor('blue')
    draw(height,color)

def draw(height,color):
    t.begin_fill()
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

def swap(c1,c2,l):
    l.insert(c1.position,c2)
    l.insert(c2.position,c1)
    #l.pop(c2.position+1)
    #l.pop(c2.position+2)


l = [5,8,6,10]
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
    collumn(item.height,item.position)
    swap(c[0],c[3],c)


for i in c:
    collumn(i.height,i.position)
    t.exitonclick()
    create(item.height,item.position)

swap(c[3],c[4])

t.exitonclick()
