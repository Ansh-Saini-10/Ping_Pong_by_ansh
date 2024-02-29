from turtle import Turtle, Screen
screen = Screen()

SCORE_FONT = ("courier", 40, "normal")
WINNER_LOSER_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = WINNER_LOSER_FONT

class Scoreboard:
    def __init__(self, coordinates):
        self.scoreboard = 0
        self.score = Turtle()
        self.score.color("white")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(coordinates)

        self.write_score()

    def write_score(self):
        self.score.clear()
        self.score.write(arg=f"{self.scoreboard}", move=False, align="center", font=SCORE_FONT)

    def update_score(self):
        self.scoreboard += 1
        self.write_score()
        screen.update()

    def does_won(self, name: str, win_or_not: bool, coordinates:tuple):
        self.score.goto(coordinates)
        results = "win" if win_or_not else "lose"
        self.score.write(arg=f"{name} {results}", font=WINNER_LOSER_FONT)

    def game_over(self, arg:str, coordinates: tuple):
        self.score.goto(coordinates)
        self.score.write(arg=arg, font=GAME_OVER_FONT)
