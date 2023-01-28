from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.seglist = []
        self.createSnake()
        self.head = self.seglist[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.seglist)-1, 0, -1):  
            newx = self.seglist[seg_num-1].xcor()  # get coordinate of segment closer to head
            newy = self.seglist[seg_num-1].ycor()
            self.seglist[seg_num].goto(newx, newy)  # replace current location with segment in front
        
        self.seglist[0].forward(MOVE_DISTANCE)  # getting head to move

    def add_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.seglist.append(seg)

    def extend(self):
        self.add_segment(self.seglist[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

