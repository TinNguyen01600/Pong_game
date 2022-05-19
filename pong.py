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
paddle_b.speed(0)   # not the speed of the paddle moving on the screen
                    # it's the speed of animation. 0 = maximum speed
paddle_b.shape('square')    # size is 20px x 20px
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    # wid = 100px, len = 20px
paddle_b.up()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)   # not the speed of the paddle moving on the screen
                    # it's the speed of animation. 0 = maximum speed
ball.shape('circle')    # size is 20px x 20px
ball.color('white')
ball.up()
ball.goto(0, 0)

# Main game loop
while(True):
    wn.update()