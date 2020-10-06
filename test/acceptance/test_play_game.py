from assertpy import assert_that
from src.domain.snake import Snake
from src.use_case.move_snake import MoveSnake
from src.use_case.show_board import ShowBoard

def test_can_move_the_snake_infinitely_across_the_board():
    board = [5, 5]
    snake = Snake([[0, 0]], 'E')
    move_snake = MoveSnake()
    show_board = ShowBoard()

    assert_that(show_board.execute(board, snake)).is_equal_to([
      ['', '', '', '', ''],
      ['', '', '', '', ''],
      ['', '', 'S', '', ''],
      ['', '', '', '', ''],
      ['', '', '', '', '']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
      ['', '', '', '', ''],
      ['', '', '', '', ''],
      ['', 'S', '', '', ''],
      ['', '', '', '', ''],
      ['', '', '', '', '']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
      ['', '', '', '', ''],
      ['', '', '', '', ''],
      ['S', '', '', '', ''],
      ['', '', '', '', ''],
      ['', '', '', '', '']
    ])
    move_snake.execute(board, snake)
    assert_that(show_board.execute(board, snake)).is_equal_to([
      ['', '', '', '', ''],
      ['', '', '', '', ''],
      ['', '', '', '', 'S'],
      ['', '', '', '', ''],
      ['', '', '', '', '']
    ])

