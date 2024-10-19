from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, paddle_offset, paddle_limit, pixel_size=20):
        super().__init__()
        self.pixel_size = pixel_size
        self.size = 3
        self.paddle_offset = paddle_offset
        self.paddle_limit = paddle_limit
        self.paddle_position = self.create_paddle()

    def create_paddle(self):
        self.up()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.size, stretch_len=1)
        self.setpos(self.paddle_offset, 0)
        paddle_position = self.position()
        return paddle_position
    
    def move_up(self):
        if self.ycor() >= self.paddle_limit:
            pass
        else:
            y=self.ycor()+self.pixel_size
            x=self.xcor()
            self.setpos(x,y)

    def move_down(self):
        if self.ycor() <= -self.paddle_limit:
            pass
        else:
            y=self.ycor()-self.pixel_size
            x=self.xcor()
            self.setpos(x,y)
        
        
