from assertpy import assert_that
from src.use_case.move_snake import MoveSnake
from src.domain.snake import Snake
from src.domain.board import Board
from src.domain.coordinate import Coordinate

stub_board = Board(width=6, height=6)


def test_move_one_unit_towards_east():
    current_location = [Coordinate(x=3, y=0)]
    current_heading = 'E'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)
    assert_that(snake.current_location[0].x).is_equal_to(4)
    assert_that(snake.current_location[0].y).is_equal_to(0)


def test_move_two_units_towards_east():
    current_location = [Coordinate(x=3, y=0)]
    current_heading = 'E'
    snake = Snake(current_location, current_heading)

    for _ in range(2):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(5)
    assert_that(snake.current_location[0].y).is_equal_to(0)


def test_move_one_unit_towards_north():
    current_location = [Coordinate(x=0, y=0)]
    current_heading = 'N'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(0)
    assert_that(snake.current_location[0].y).is_equal_to(1)


def test_move_one_unit_towards_west():
    current_location = [Coordinate(x=2, y=0)]
    current_heading = 'W'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(1)
    assert_that(snake.current_location[0].y).is_equal_to(0)


def test_move_one_unit_towards_south():
    current_location = [Coordinate(x=0, y=3)]
    current_heading = 'S'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(0)
    assert_that(snake.current_location[0].y).is_equal_to(2)


def test_move_infinitely_towards_east():
    current_location = [Coordinate(x=5, y=0)]
    current_heading = 'E'
    snake = Snake(current_location, current_heading)

    for _ in range(3):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(2)
    assert_that(snake.current_location[0].y).is_equal_to(0)


def test_move_infinitely_towards_north():
    current_location = [Coordinate(x=0, y=5)]
    current_heading = 'N'
    snake = Snake(current_location, current_heading)

    for _ in range(3):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(0)
    assert_that(snake.current_location[0].y).is_equal_to(2)


def test_move_infinitely_towards_west():
    current_location = [Coordinate(x=0, y=0)]
    current_heading = 'W'
    snake = Snake(current_location, current_heading)

    for _ in range(3):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(3)
    assert_that(snake.current_location[0].y).is_equal_to(0)


def test_move_infinitely_towards_south():
    current_location = [Coordinate(x=0, y=0)]
    current_heading = 'S'
    snake = Snake(current_location, current_heading)

    for _ in range(3):
        MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(0)
    assert_that(snake.current_location[0].y).is_equal_to(3)


def test_body_can_follow_the_head():
    current_location = [
        Coordinate(x=0, y=0),
        Coordinate(x=1, y=0),
        Coordinate(x=2, y=0)
    ]
    current_heading = 'W'
    snake = Snake(current_location, current_heading)

    MoveSnake().execute(stub_board, snake)

    assert_that(snake.current_location[0].x).is_equal_to(5)
    assert_that(snake.current_location[0].y).is_equal_to(0)
    assert_that(snake.current_location[1].x).is_equal_to(0)
    assert_that(snake.current_location[1].y).is_equal_to(0)
    assert_that(snake.current_location[2].x).is_equal_to(1)
    assert_that(snake.current_location[2].y).is_equal_to(0)
