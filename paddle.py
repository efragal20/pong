from turtle import Turtle, Screen
class Paddle():
    def __init__(self, paddle_offset, pixel_size=20):
        self.pixel_size = pixel_size
        self.size = 4
        self.paddle_offset = paddle_offset
        self.create_paddle()

    def create_paddle(self):
        self.segments = self.create_paddle_segments()
        self.y_pos = 0
        for segments_paddles in self.segments:
            segments_paddles.up()
            segments_paddles.setpos(self.paddle_offset, self.y_pos)
            self.y_pos+=20
            segments_paddles.seth(270)
    
    def move_up(self, screen):
        for segment in self.segments:
            segment.seth(90)
        self.refresh_paddle(screen)

    def move_down(self, screen):
        for segment in self.segments:
            segment.seth(270)
        self.refresh_paddle(screen)

    def refresh_paddle(self, screen):
        for segment in self.segments:
            segment.forward(self.pixel_size)
        screen.update()
        
    def create_paddle_segments(self):
        paddle = []
        for segment in range(0,self.size):
            new_segment = Turtle("square")
            new_segment.color("white")
            paddle.append(new_segment)
        print(paddle)
        return paddle
