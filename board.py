from turtle import Turtle, Screen

class Board():
    def __init__(self, pixel_size = 20):
        super().__init__()
        self.screen = Screen()
        self.pixel_size = pixel_size
        self.drawer = Turtle()
        self.screen_size = {"x": 800, "y": 600}
        self.line_lenght = 10
        self.line_width = 10

    def draw_field_pong(self):
        self.screen.setup(width=self.screen_size["x"], height = self.screen_size["y"],startx=400, starty=200)
        self.screen.bgcolor("black")
        self.screen.title("PONG GAME")
        self.screen.tracer(0)
        self.screen.listen()
        self.drawer.up()
        self.drawer.color("white")
        self.drawer.setpos(0, self.screen_size["y"]/2)
        self.drawer.seth(270)
        self.drawer.width = self.line_width
        for segment in range(0,50):
            self.drawer.down()
            self.drawer.forward(self.line_lenght)
            self.drawer.up()
            self.drawer.forward(self.line_lenght)

