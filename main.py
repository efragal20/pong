from board import Board
from paddle import Paddle

pong_game_board = Board()
pong_game_board.draw_field_pong()

paddle_offset = abs(pong_game_board.screen_size["x"]/2)-pong_game_board.pixel_size
paddle_limit = abs(pong_game_board.screen_size["y"]/2)-2*pong_game_board.pixel_size
pong_game_board.draw_score(left_score=0, right_score=0)

paddle_left = Paddle(paddle_offset=-paddle_offset, paddle_limit=paddle_limit)
# print(f"La posicion de la raqueta izquierda: {paddle_left.paddle_position}")
paddle_right = Paddle(paddle_offset=paddle_offset, paddle_limit=paddle_limit)
# print(f"La posicion de la raqueta derecha: {paddle_right.paddle_position}")
position_paddle_left = abs(paddle_left.paddle_position)
position_paddle_right = abs(paddle_right.paddle_position)
pong_game_board.draw_ball(position_paddle_left, position_paddle_right) #Ball

pong_game_board.screen.onkeypress(fun=paddle_left.move_up, key="w")
pong_game_board.screen.onkeypress(fun=paddle_left.move_down, key="s")
pong_game_board.screen.onkeypress(fun=paddle_right.move_up, key="Up")
pong_game_board.screen.onkeypress(fun=paddle_right.move_down, key="Down")

pong_game_board.screen.exitonclick()