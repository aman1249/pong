import turtle 

wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer()
wn.title("pong")
wn.setup(width=800, height=600)

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-360, 0)
paddle_a.penup()
paddle_a.color("white")

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(360, 0)
paddle_b.penup()
paddle_b.color("white")

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.goto(0, 0)
ball.penup()
ball.color("white")

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)



while True:
    wn.update()