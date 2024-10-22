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

paddle_left = Paddle(paddle_offset=-paddle_offset, paddle_limit=paddle_limit, board=pong_game_board)
# print(f"La posicion de la raqueta izquierda: {paddle_left.paddle_position}")
paddle_right = Paddle(paddle_offset=paddle_offset, paddle_limit=paddle_limit, board=pong_game_board)
# print(f"La posicion de la raqueta derecha: {paddle_right.paddle_position}")

ball = Ball(board=pong_game_board)
ball.move_ball(x_limit=board_size["x"]/2, y_limit=board_size["y"]/2) #Ball

pong_game_board.screen.onkeypress(fun=paddle_left.move_up, key="w")
pong_game_board.screen.onkeypress(fun=paddle_left.move_down, key="s")
pong_game_board.screen.onkeypress(fun=paddle_right.move_up, key="Up")
pong_game_board.screen.onkeypress(fun=paddle_right.move_down, key="Down")

pong_game_board.screen.exitonclick()