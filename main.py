from board import Board
from paddle import Paddle

pong_game_board = Board()
paddle = Paddle()

pong_game_board.draw_field_pong()
paddles=paddle.create_paddle_segments()
paddle.create_paddle(paddles)


pong_game_board.screen.exitonclick()