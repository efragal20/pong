from turtle import Turtle, Screen
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
                segments_paddles.seth(270)
            self.refresh_paddel(paddle)
        elif side.lower() == "right":
            pass
        else:
            print(f"Wrong side: {side}, left or right allowed")

    def refresh_paddel(self, paddle):
        paddle_lenght=len(paddle)
        game=True
        while game:
            for index in range(1,paddle_lenght):
                new_paddle_pos = paddle[-index-1].pos()
                paddle[-index].setpos(new_paddle_pos)
            paddle[0].forward(20)
        
    def create_paddle_segments(self):
        paddle = []
        for segment in range(0,self.size):
            new_segment = Turtle("square")
            new_segment.color("white")
            paddle.append(new_segment)
        print(paddle)
        return paddle
