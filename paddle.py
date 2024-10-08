from turtle import Turtle

class Paddle():
    def __init__(self):
        self.size = 4
    
    def create_paddles(self):
        self.left_paddle = self.create_paddle_segments()
        self.right_paddle = self.create_paddle_segments()
    
    def create_paddle_segments(self):
        paddle = []
        for segment in range(0,self.size):
            new_segment = Turtle("square")
            new_segment.color("white")
            paddle.append(new_segment)
        return paddle