import turtle
from time import sleep

from insertion_sort import sort

# t = turtle.Turtle()
# t.pencolor("black")
screen = turtle.Screen()
screen.tracer(0)
# name.screensize(bg="black", canvheight=650, canvwidth=700)
# name.setup(width=1.0, height=1.0, starty=0, startx=0)
screen.setup(height=650, width=700)
screen.setworldcoordinates(llx=0, urx=700, lly=-650 // 2, ury=650 // 2)
screen.bgcolor("black")
screen.title("Graphical view of insertion Sort ")


class Column:
    def __init__(self, height: int, position: int, color: str = "blue"):
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
        # if position < 35:
        #     position = -700 + 31 * position
        # else:
        #     position = 700 - 31 * position
        self._t.goto(position * 21, 0)
        if max_height is not None:
            color = self._t.color()[0]
            self._t.color("black")
            self._draw(max_height)
            self._t.color(color)
        self._draw(height)

    def _draw(self, height: int):
        self._t.begin_fill()
        self._t.pendown()
        self._t.forward(20)
        self._t.left(90)
        self._t.forward(10 * height)
        self._t.left(90)
        self._t.forward(20)
        self._t.left(90)
        self._t.forward(10 * height)
        self._t.left(90)
        self._t.end_fill()
        self._t.penup()
        self._t.screen.update()

    def set_color(self, color):
        self._t.color(color)
        print(color)
        self._draw(self._height)

    def get_height(self):
        return self._height

    def get_position(self):
        return self._position

    def set_position(self, pos: int, max_height: int):
        self._position = pos
        self._create(self._height, self._position, max_height=max_height)


l = [5, 8, 6, 30, 10, 25, 17, 23, 15, 9, 22, 18, 4, 1]
columns = [Column(i, p) for p, i in enumerate(l)]
sleep(5)
sort(columns)
# pos = 0

# for item in l:
#     create(item, pos)
#     pos += 1
# i = 4
# swap(l[i - 1], l[i])
# πρώτα να βρούμε τρόπο να αλλάζει το χρώμα της επιλεγμένης μπάρας
screen.exitonclick()
