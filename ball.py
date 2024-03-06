from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(self.random_heading())
        self.default_ball_speed = 5
        self.ball_speed = self.default_ball_speed

    def move(self):
        self.forward(self.ball_speed)
        # print(self.ball_speed)
        time.sleep(0.01)

    def bounce(self):
        self.setheading(self.heading() * -1)
        self.move()

    def bounce_from_paddle(self):
        self.setheading(180 - self.heading())
        self.move()

    def ball_reset(self):
        self.ball_speed = self.default_ball_speed
        self.goto(x=0, y=0)
        self.setheading(self.heading() + random.randint(120, 180))

    def random_heading(self) -> int:
        random_num = random.randint(25, 80)
        left_or_right = 1
        return random_num if left_or_right else (random_num + 180)
    
    def increase_speed(self):
        self.ball_speed += 0.5
    