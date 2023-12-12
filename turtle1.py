def turtle1(l):
    #the graphical view of insertion sort
    import random
    import turtle
    from time import sleep
    from insertion_sort import sort

    #creating a screen object and modifying it to our needs (color,size...)
    screen = turtle.Screen()
    screen.tracer(0, 0)
    screen.setup(height=1.0, width=1.0)
    screen.setworldcoordinates(llx=0, urx=700, lly=0, ury=650)
    screen.bgcolor("black")
    screen.title("Graphical view of insertion Sort ")

    class Column:
        #creates "column" items with attributes height, position and color
        def __init__(self, height: int, position: int, color: str = "white"):
            self._height = height
            self._position = position
            self._t = turtle.Turtle() #creates the turtle object
            self._t.color(color)
            self._create(self._height, self._position)

        def _create(self, height: int, position: int, max_height=None):
            #creates the column in turtle
            self._t.hideturtle()
            self._t.penup()
            self._t.goto(position * (701/len(l)),0) #the position on the canvas is calculated through a mathematical equation
            if max_height is not None:
                """If a max_height is given (through the set_position func)
                the turtle creates a black column/erases the one existing in the current position
                allowing for the creation of a smaller one"""
                color = self._t.color()[0]
                self._t.color("black")
                self._draw(max_height, False)
                self._t.color(color)
            self._draw(height)

        def _draw(self, height: int, update=True):
            #function that draws the rectangle
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
            #changes the color of the column
            self._t.color(color)
            self._draw(self._height, False)

        def get_height(self):
            #returns the value of the specified column (height)
            return self._height

        def get_position(self):
            #returns the position of the specified column (list pos)
            return self._position

        def set_position(self, pos: int, max_height: int):
            #creates a column at a specified position
            #used change the position of a column
            self._position = pos
            self._create(self._height, self._position, max_height=max_height)

    columns=[Column(i,p) for p,i in enumerate(l)] #using the list given it makes a list of Column items
    sort(columns)
    screen.exitonclick()