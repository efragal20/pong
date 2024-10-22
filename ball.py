from turtle import Turtle
import random
from time import sleep

vertical_directions = ["up", "down"]
horizontal_directions = ["left", "right"]

class Ball(Turtle):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.initial_pos = (0,0)
        self.initial_direction = { "horizontal": random.choice(horizontal_directions), "vertical": random.choice(vertical_directions) }
        self.current_direction = self.initial_direction 
        self.ball_movement = True

        self.speed(1)
        self.up()
        self.shape("circle")
        self.color("white")

        self.set_direction()
        self.setpos(self.initial_pos)

    def set_direction(self):
        if self.current_direction["vertical"] == "up" and  self.current_direction["horizontal"] == "right":
            self.seth(45)
        elif self.current_direction["vertical"] == "up" and  self.current_direction["horizontal"] == "left":
            self.seth(135)
        elif self.current_direction["vertical"] == "down" and  self.current_direction["horizontal"] == "right":
            self.seth(-45)
        elif self.current_direction["vertical"] and  self.current_direction["horizontal"] == "left":
            self.seth(-135)
    
    def opposite(direction):
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        return opposites.get(direction)
        

    def bounce(self, bounce_wall):
        if bounce_wall in vertical_directions:
            self.current_direction["vertical"] = Ball.opposite(bounce_wall)
        elif bounce_wall in horizontal_directions:
            self.current_direction["horizontal"] = Ball.opposite(bounce_wall)
        self.set_direction()
        

    def move_ball(self, x_limit, y_limit):
        while self.ball_movement:
            self.forward(10)
            sleep(0.02)
            if  abs(self.xcor()) >= x_limit:
                self.bounce(self.current_direction["horizontal"])
            elif  abs(self.ycor()) >= y_limit:
                self.bounce(self.current_direction["vertical"])
            self.board.screen.update()