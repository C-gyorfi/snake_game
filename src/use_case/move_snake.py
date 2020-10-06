class MoveSnake:
    @staticmethod
    def execute(board, snake):
        head_location = snake.current_location[0]
        board_width = board[0]
        if snake.current_heading == 'E':
            head_location = [
                head_location[0] - 1, head_location[1]]
            if head_location[0] == -1:
                head_location[0] = board_width - 1
        elif snake.current_heading == 'N':
            head_location = [
                head_location[0], head_location[1] + 1]
        elif snake.current_heading == 'W':
            head_location = [
                head_location[0] + 1, head_location[1]]
        elif snake.current_heading == 'S':
            head_location = [
                head_location[0], head_location[1] - 1]
        snake.current_location[0] = head_location
