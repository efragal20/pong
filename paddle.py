from turtle import Turtle

class Paddle():
    def __init__(self):
        self.size = 4
    
    def create_paddle(self, side):
        if side.lower() == "left":
            
        elif side.lower == "right":

        else
            print(f"Wrong side: {side}, left or right allowed")
    
    def create_paddle_segments(self):
        paddle = []
        for segment in range(0,self.size):
            new_segment = Turtle("square")
            new_segment.color("white")
            paddle.append(new_segment)
        return paddle