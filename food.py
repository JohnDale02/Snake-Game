from turtle import Turtle
import random

EDGES = 250

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-EDGES, EDGES)
        random_y = random.randint(-EDGES, EDGES)
        self.goto(random_x, random_y)

