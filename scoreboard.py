from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.TEXT_X = 0
        self.TEXT_Y = 270
        self.FONTSIZE = 24
        self.ALIGN = "center"
        self.score = 0 
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(self.TEXT_X, self.TEXT_Y)
        self.update_scoreboard()
       

    def update_scoreboard(self):
       self.write(f"Score: {self.score}", align=self.ALIGN, font=("Courier", self.FONTSIZE, "normal"))
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def display_game_over(self):
        for iteration in range(0, 50):
            self.TEXT_Y -= 7
            self.FONTSIZE += 1
            self.clear()
            self.goto(self.TEXT_X, self.TEXT_Y)
            self.update_scoreboard()
            self.goto(0,50)
            self.write("GAME OVER", align=self.ALIGN, font=("Courier", self.FONTSIZE, "normal"))



