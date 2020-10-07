class MoveSnake:
    @staticmethod
    def execute(board, snake):
        head_location = MoveSnake.move_head(snake)
        MoveSnake.wrap_around_borders(board, head_location)
        MoveSnake.update_location(snake, head_location)

    @staticmethod
    def move_head(snake):
        head_location = snake.current_location[0]
        if snake.current_heading == 'E':
            head_location = [
                head_location[0] + 1, head_location[1]]
        elif snake.current_heading == 'N':
            head_location = [
                head_location[0], head_location[1] + 1]
        elif snake.current_heading == 'W':
            head_location = [
                head_location[0] - 1, head_location[1]]
        elif snake.current_heading == 'S':
            head_location = [
                head_location[0], head_location[1] - 1]
        return head_location

    @staticmethod
    def wrap_around_borders(board, location):
        board_width = board[0]
        board_height = board[1]
        location[0] = 0 if location[0] == board_width else location[0]
        location[1] = 0 if location[1] == board_height else location[1]
        location[0] = board_width - 1 if location[0] == -1 else location[0]
        location[1] = board_height - 1 if location[1] == -1 else location[1]

    @staticmethod
    def update_location(snake, head_location):
        snake.current_location.insert(0, head_location)
        snake.current_location.pop()
