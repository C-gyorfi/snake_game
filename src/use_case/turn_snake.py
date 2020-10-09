class TurnSnake:
    DIRECTIONS = ['W', 'N', 'E', 'S']

    @staticmethod
    def execute(dir, snake):
        if TurnSnake.can_be_a_valid_turn(dir, snake.current_heading):
            snake.current_heading = dir

    @staticmethod
    def can_be_a_valid_turn(dir, heading):
        index_of_left_turn = TurnSnake.DIRECTIONS.index(heading) - 1
        index_of_right_turn = TurnSnake.DIRECTIONS.index(heading) + 1
        index_of_right_turn = index_of_right_turn if index_of_right_turn < 4 else 0
        return TurnSnake.DIRECTIONS[index_of_left_turn] == dir or TurnSnake.DIRECTIONS[index_of_right_turn] == dir
