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

        self.start_round()
    
    def start_round(self):
        self.initial_direction = { "horizontal": random.choice(horizontal_directions), "vertical": random.choice(vertical_directions) }
        self.setpos(self.initial_pos)
        self.set_direction()
        
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
        

    def bounce_on_paddle(self, paddle):
        vertical_limits = paddle.get_vertical_limits()
        if vertical_limits[0] <= self.ycor() <= vertical_limits[1]:
            self.bounce(self.current_direction["horizontal"])

    def move_ball(self, x_limit, y_limit, left_paddle, right_paddle, pixel_size):
        while self.ball_movement:
            self.forward(10)
            sleep(0.07)

            if self.current_direction["horizontal"] == "right":
                paddle_to_bounce = right_paddle
                point_to = left_paddle
            else:
                paddle_to_bounce = left_paddle
                point_to = right_paddle
            
            if abs(self.xcor()) >= x_limit:
                point_to.score_goal()
                self.board.draw_score(left_paddle.score, right_paddle.score)
                self.start_round()
                break

            if  abs(self.xcor()) >= x_limit-2*pixel_size:
                self.bounce_on_paddle(paddle_to_bounce)
            elif  abs(self.ycor()) >= y_limit:
                self.bounce(self.current_direction["vertical"])

            self.board.screen.update()