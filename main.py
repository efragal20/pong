from board import Board
from paddle import Paddle
from ball import Ball

board_size = {"x": 800, "y": 600}
pixel_size = 20
pong_game_board = Board(pixel_size=pixel_size, screen_size = board_size)
pong_game_board.draw_field_pong()

paddle_offset = abs(board_size["x"]/2)-pixel_size
paddle_limit = abs(board_size["y"]/2)-2*pixel_size
pong_game_board.draw_score(left_score=0, right_score=0)

left_paddle = Paddle(paddle_offset=-paddle_offset, paddle_limit=paddle_limit, board=pong_game_board)
# print(f"La posicion de la raqueta izquierda: {left_paddle.paddle_position}")
right_paddle = Paddle(paddle_offset=paddle_offset, paddle_limit=paddle_limit, board=pong_game_board)
# print(f"La posicion de la raqueta derecha: {right_paddle.paddle_position}")

pong_game_board.screen.onkeypress(fun=left_paddle.move_up, key="w")
pong_game_board.screen.onkeypress(fun=left_paddle.move_down, key="s")
pong_game_board.screen.onkeypress(fun=right_paddle.move_up, key="Up")
pong_game_board.screen.onkeypress(fun=right_paddle.move_down, key="Down")

ball = Ball(board=pong_game_board)

def start():
    ball.move_ball(x_limit=board_size["x"]/2, y_limit=board_size["y"]/2, left_paddle=left_paddle, right_paddle=right_paddle, pixel_size=pixel_size) #Ball

pong_game_board.screen.onkeypress(fun=start, key="space")


pong_game_board.screen.exitonclick()