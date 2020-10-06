class MoveSnake:
  def execute(self, board, snake):
    if snake.current_heading == 'E':
      snake.current_location[0] = [snake.current_location[0][0] -1, snake.current_location[0][1]]
    else:
      snake.current_location[0] = [snake.current_location[0][0], snake.current_location[0][1] + 1]
