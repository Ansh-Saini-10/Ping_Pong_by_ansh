from turtle import Screen, Turtle
from Pong import Paddle
from ball import Ball
from score import Scoreboard
import time
import random

# =============================== Background functions and stuff ============================
my_bg_colors = ["#000", "#337357", "#FF3EA5", "#1D2B53", "#900C3F", "#FAA300", "#2e4242"]


def change_bg_color(colors: list) -> str:
    chosen_color = random.choice(colors)
    return chosen_color

# ======================================== Screen ===========================================
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(change_bg_color(my_bg_colors))
screen.title("Ping Pong by Ansh")

screen.tracer(0)

middle_line = Turtle()
middle_line.color("white")
middle_line.pensize(10)
middle_line.penup()
middle_line.hideturtle()
middle_line.goto(x=0, y=300)

for _ in range(15):
    middle_line.pendown()
    middle_line.sety(middle_line.ycor() - 20)
    middle_line.penup()
    middle_line.sety(middle_line.ycor() - 20)


# =================================== Coordinates for Paddles=====================================
Left_Paddle_cor = (-350, 0)
Right_Paddle_cor = (350, 0)

# ==================================== Coordinates for Who won ===================================
# I really suck at naming things, sorry for that
p1_results_coord = (-250, -140)
p2_results_coord = (150, -140)

# ======================================= Creating Objects =======================================

left_paddle = Paddle(Left_Paddle_cor)
right_paddle = Paddle(Right_Paddle_cor)

ball = Ball()

p1_score_coordinates = (-45, 240)
p2_score_coordinates = (45, 240)

p1_score = Scoreboard(p1_score_coordinates)
p2_score = Scoreboard(p2_score_coordinates)

screen.update()

p1_score.write_score()
p2_score.write_score()

# ============================================== Controls ===========================================

screen.listen()

screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")

screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")

screen.onkey(fun=ball.ball_reset, key="Return")

screen.onkeypress(fun=screen.bye, key="0") # For debugging

# ========================================= Main/Complex Things =======================================

SCORE_NEED_TO_WIN = 5

def game():
    while True:
        screen.update()

        if p1_score.scoreboard >= SCORE_NEED_TO_WIN or SCORE_NEED_TO_WIN <= p2_score.scoreboard:
            p1_score.does_won(name="P1",
                            win_or_not=(p1_score.scoreboard > p2_score.scoreboard),
                            coordinates=p1_results_coord)
            
            p2_score.does_won(name="P2",
                            win_or_not=(p2_score.scoreboard > p1_score.scoreboard),
                            coordinates=p2_results_coord)

            p1_score.game_over(arg="Press Space to Play Again", coordinates=(-180, -230))

            return

        if ball.xcor() >= 340 or ball.xcor() <= -340:
            if ball.distance(left_paddle) <= 80 or ball.distance(right_paddle) <= 80:
                ball.bounce_from_paddle()
                ball.ball_speed += 0.05
                screen.bgcolor(change_bg_color(my_bg_colors))
            else:
                p1_score.update_score() if ball.xcor() >= 340 else p2_score.update_score()

                for _ in range(100):
                    ball.move()
                    screen.update()

                ball.ball_reset()
                screen.update()
                time.sleep(1)

        elif 285 <= ball.ycor() or ball.ycor() <= -285:
            ball.bounce()
            screen.bgcolor(change_bg_color(my_bg_colors))


        ball.move()
        screen.update()


game()


def restart_game():
    global p1_score, p2_score

    ball.ball_reset()
    ball.ball_speed = ball.default_ball_speed

    p1_score.game_init()
    p2_score.game_init()

    game()


screen.onkeypress(fun=restart_game, key="space")

screen.exitonclick()
