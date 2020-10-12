from src.domain.coordinate import Coordinate


class MoveSnake:
    @staticmethod
    def execute(board, snake, food=None):
        new_head_location = MoveSnake.move_head(snake)
        new_head_location = MoveSnake.wrap_around_borders(
            board, new_head_location)
        return MoveSnake.update_location(snake, new_head_location, food)

    @staticmethod
    def move_head(snake):
        head_location = Coordinate(
            x=snake.current_location[0].x,
            y=snake.current_location[0].y
        )
        if snake.current_heading == 'E':
            head_location.x = head_location.x + 1
        elif snake.current_heading == 'N':
            head_location.y = head_location.y + 1
        elif snake.current_heading == 'W':
            head_location.x = head_location.x - 1
        elif snake.current_heading == 'S':
            head_location.y = head_location.y - 1
        return head_location

    @staticmethod
    def wrap_around_borders(board, location):
        location.x = 0 if location.x == board.width else location.x
        location.y = 0 if location.y == board.height else location.y
        location.x = board.width - 1 if location.x == -1 else location.x
        location.y = board.height - 1 if location.y == -1 else location.y
        return location

    @staticmethod
    def update_location(snake, new_head_location, food):
        snake.current_location.insert(0, new_head_location)

        if MoveSnake.can_feed_snake(food, new_head_location):
            food.pop()
            return snake
        snake.current_location.pop()
        return snake

    @staticmethod
    def can_feed_snake(food, head_location):
        if not food:
            return False
        else:
            return head_location.x == food[0].x and head_location.y == food[0].y
