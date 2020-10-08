from assertpy import assert_that
from src.domain.snake import Snake
from src.use_case.move_snake import MoveSnake
from src.use_case.show_board import ShowBoard
from src.domain.board import Board


def test_can_move_the_snake_infinitely_across_the_board():
    board = Board(width=5, height=5)
    snake = Snake([[0, 0]], 'W')
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['O', '', '', '', '']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', 'O']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', 'O', '']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', 'O', '', '']
    ])


def test_can_move_the_snake_infinitely_across_any_size_of_board():
    board = Board(width=6, height=3)
    snake = Snake([[0, 0]], 'W')
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['O', '', '', '', '', '']
    ])
    for i in range(3):
        move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', 'O', '', '']
    ])
