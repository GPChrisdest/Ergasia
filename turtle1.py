import random
import turtle
from time import sleep
from insertion_sort import sort

screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(height=1.0, width=1.0)
screen.setworldcoordinates(llx=0, urx=700, lly=0, ury=650)
screen.bgcolor("black")
screen.title("Graphical view of insertion Sort ")


class Column:
    def __init__(self, height: int, position: int, color: str = "white"):
        self._height = height
        self._position = position
        self._t = turtle.Turtle()
        if color is not None:
            self._t.color(color)
        self._create(self._height, self._position)

    def _create(self, height: int, position: int, max_height=None):
        # canvas 700x650
        self._t.hideturtle()
        self._t.speed(0)
        self._t.penup()
        self._t.goto(position * (701/len(l)),0)
        if max_height is not None:
            color = self._t.color()[0]
            self._t.color("black")
            self._draw(max_height, False)
            self._t.color(color)
        self._draw(height)

    def _draw(self, height: int, update=True):
        self._t.begin_fill()
        self._t.pendown()
        self._t.forward(701/len(l) - 1)
        self._t.left(90)
        self._t.forward(10 * height)
        self._t.left(90)
        self._t.forward(701/len(l) - 1)
        self._t.left(90)
        self._t.forward(10 * height)
        self._t.left(90)
        self._t.end_fill()
        self._t.penup()
        if update == True:
            self._t.screen.update()

    def set_color(self, color):
        self._t.color(color)
        self._draw(self._height, False)

    def get_height(self):
        return self._height

    def get_position(self):
        return self._position

    def set_position(self, pos: int, max_height: int):
        self._position = pos
        self._create(self._height, self._position, max_height=max_height)

l = []
for u in range(40):
    u = random.randint(1,40)
    if not u in l:
        l.append(u)

columns = [Column(i, p) for p, i in enumerate(l)]
sleep(3)
print(l)
sort(columns)
print(sorted(l))
screen.exitonclick()
