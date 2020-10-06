from assertpy import assert_that
from src.use_case.move_snake import MoveSnake
from src.domain.snake import Snake

stub_board = [6, 6]


def test_move_one_unit_towards_east():
    current_location = [[3, 0]]
    current_heading = 'E'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)
    assert_that(snake.current_location).is_equal_to([[2, 0]])


def test_move_two_units_towards_east():
    current_location = [[3, 0]]
    current_heading = 'E'
    snake = Snake(current_location, current_heading)

    for _ in range(2):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location).is_equal_to([[1, 0]])


def test_move_one_unit_towards_north():
    current_location = [[0, 0]]
    current_heading = 'N'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location).is_equal_to([[0, 1]])
