import turtle

t = turtle.Turtle()
t.pencolor('black')
name=turtle.Screen()
turtle.screensize(bg="black")
turtle.setup(width=1.0,height=1.0)
name.title('Graphical view of insertion Sort ')

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
    create(c1,i-1,'black')
    create(c2,i-1)
    create(c1,i)

l = [5,8,6,30,10,25,17,23,15,9]
pos = 0

for item in l:
    create(item,pos)
    pos+=1
i = 4
swap(l[i-1],l[i])
#πρώτα να βρούμε τρόπο να αλλάζει το χρώμα της επιλεγμένης μπάρας
turtle.exitonclick()