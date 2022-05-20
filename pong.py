import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600) #0;0 is the center with edges (-400, 400) and (-300, 300)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   # not the speed of the paddle moving on the screen
                    # it's the speed of animation. 0 = maximum speed
paddle_a.shape('square')    # size is 20px x 20px
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # wid = 100px, len = 20px
paddle_a.up()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')    # size is 20px x 20px
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    # wid = 100px, len = 20px
paddle_b.up()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')    # size is 20px x 20px
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Seperate ball movement into x and y
ball.dx = 2 # d means delta (change)
ball.dy = 2 # every time the ball moves, it moves by 2px (up and right)

# Function
def paddle_a_up():
    y = paddle_a.ycor() # returns the y-coordinate of paddle_a
                        # y increases when we go up and decreases when go down
    y += 20 # add 20px to y-coordinate
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
    
# Keyboard binding
wn.listen()     # tells the program to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # when "w" is pressed, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while(True):
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #reverse the ball's direction
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    