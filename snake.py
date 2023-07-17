from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
Down=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.creat_snake()
        self.head=self.segments[0]

    def creat_snake(self):
        for p in STARTING_POSITIONS:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(p)
            self.segments.append(seg)
    def add_seg(self,position):
        new=Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segments.append(new)
    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for i in range(len( self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!= Down:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(Down)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)








