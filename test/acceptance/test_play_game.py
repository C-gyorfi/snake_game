from assertpy import assert_that
from src.domain.snake import Snake
from src.use_case.move_snake import MoveSnake
from src.use_case.turn_snake import TurnSnake
from src.use_case.show_board import ShowBoard
from src.domain.board import Board
from src.domain.coordinate import Coordinate


def test_can_move_the_snake_infinitely_across_the_board():
    board = Board(width=5, height=5)
    snake = Snake([Coordinate(x=0, y=0)], 'W')
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['■', ' ', ' ', ' ', ' ']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '■']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '■', ' ']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '■', ' ', ' ']
    ])


def test_can_move_the_snake_infinitely_across_any_size_of_board():
    board = Board(width=6, height=3)
    snake = Snake([Coordinate(x=0, y=0)], 'W')
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['■', ' ', ' ', ' ', ' ', ' ']
    ])
    for i in range(3):
        move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '■', ' ', ' ']
    ])


def test_can_move_any_size_of_snake_infinitely_across_the_board():
    board = Board(width=6, height=3)
    snake = Snake(
        [
            Coordinate(x=0, y=0),
            Coordinate(x=1, y=0),
            Coordinate(x=2, y=0)
        ],
        'W'
    )
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['■', '◙', '◙', ' ', ' ', ' ']
    ])
    for i in range(3):
        move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '■', '◙', '◙']
    ])


def test_can_turn_the_snake_in_any_direction():
    board = Board(width=4, height=4)
    snake = Snake(
        [
            Coordinate(x=0, y=0),
            Coordinate(x=3, y=0),
        ],
        'E'
    )
    move_snake = MoveSnake()
    turn_snake = TurnSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        ['■', ' ', ' ', '◙']
    ])
    turn_snake.execute('N', snake)
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        ['■', ' ', ' ', ' '],
        ['◙', ' ', ' ', ' ']
    ])
    turn_snake.execute('E', snake)
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        ['◙', '■', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ])
    turn_snake.execute('N', snake)
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', ' ', ' ', ' '],
        [' ', '■', ' ', ' '],
        [' ', '◙', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ])
    turn_snake.execute('S', snake)
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        [' ', '■', ' ', ' '],
        [' ', '◙', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ])
