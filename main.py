from board import Board
from paddle import Paddle

pong_game_board = Board()
pong_game_board.draw_field_pong()

paddle_offset = abs(pong_game_board.screen_size["x"]/2)-pong_game_board.pixel_size

paddle_left = Paddle(paddle_offset=-paddle_offset)
paddle_right = Paddle(paddle_offset=paddle_offset)

pong_game_board.screen.onkey(fun=paddle_left.move_up(pong_game_board.screen), key="w")
pong_game_board.screen.onkey(fun=paddle_left.move_down(pong_game_board.screen), key="s")
pong_game_board.screen.onkey(fun=paddle_right.move_up(pong_game_board.screen), key="Up")
pong_game_board.screen.onkey(fun=paddle_right.move_down(pong_game_board.screen), key="Down")


pong_game_board.screen.exitonclick()