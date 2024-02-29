from turtle import Screen, Turtle
screen = Screen()

class Paddle(Turtle):
    def __init__(self, paddle_xcor):
        super().__init__()

        self.shape("square")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.goto(paddle_xcor)
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.showturtle()

    def go_up(self):
        self.forward(20)
        screen.update()

    def go_down(self):
        self.backward(20)
        screen.update()


