import pytest
from assertpy import assert_that
from src.use_case.show_board import ShowBoard
from src.domain.snake import Snake
from src.domain.board import Board


@pytest.mark.parametrize("current_location,board,expected_board", [
    ([[2, 2]], Board(width=5, height=5),
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', 'O', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([[0, 0]], Board(width=5, height=5),
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['O', '', '', '', '']
    ]
    ),
    ([[0, 4]], Board(width=5, height=5),
        [
            ['O', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([[3, 4]], Board(width=5, height=5),
     [
        ['', '', '', 'O', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ]
    ),
    ([[0, 0]], Board(width=1, height=1),
     [
        ['O']
    ]
    ),
    ([[2, 2]], Board(width=3, height=3),
     [
        ['', '', 'O'],
        ['', '', ''],
        ['', '', '']
    ]
    ),
])
def test_can_draw_a_board_with_snake(
        current_location,
        board,
        expected_board):
    snake = Snake(current_location, 'Dummy')

    board = ShowBoard().execute(board, snake)
    assert_that(board).is_equal_to(expected_board)
