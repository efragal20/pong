from turtle import Turtle
class Paddle():
    def __init__(self):
        self.size = 4

    def create_paddle(self, paddle):
        side=input("Choise your lado: ")
        if side.lower() == "left":
            y = 0
            for segments_paddles in paddle:
                segments_paddles.up()
                segments_paddles.setpos(-200, y)
                y+=20
        elif side.lower() == "right":
            pass
        else:
            print(f"Wrong side: {side}, left or right allowed")

    def create_paddle_segments(self):
        paddle = []
        for segment in range(0,self.size):
            new_segment = Turtle("square")
            new_segment.color("white")
            paddle.append(new_segment)
        print(paddle)
        return paddle
