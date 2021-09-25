import turtle 

wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer()
wn.title("pong")
wn.setup(width=800, height=600)
#every game needs loop
#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-360, 0)
paddle_a.penup()
paddle_a.color("white")
#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(360, 0)
paddle_b.penup()
paddle_b.color("white")
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.goto(0, 0)
ball.penup()
ball.color("white")
#commands
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")


while True:
    wn.update()