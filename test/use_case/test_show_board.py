import pytest
from assertpy import assert_that
from src.use_case.show_board import ShowBoard
from src.domain.snake import Snake


@pytest.mark.parametrize("current_location,stub_board,expected_board", [
    ([[2, 2]], [5, 5],
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', 'O', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([[0, 0]], [5, 5],
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['O', '', '', '', '']
    ]
    ),
    ([[0, 4]], [5, 5],
        [
            ['O', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([[3, 4]], [5, 5],
     [
        ['', '', '', 'O', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ]
    ),
    ([[0, 0]], [1, 1],
     [
        ['O']
    ]
    ),
])
def test_can_draw_a_board_with_snake(
        current_location,
        stub_board,
        expected_board):
    snake = Snake(current_location, 'Dummy')

    board = ShowBoard().execute(stub_board, snake)
    assert_that(board).is_equal_to(expected_board)
