import pytest
from assertpy import assert_that
from src.use_case.show_board import ShowBoard
from src.domain.snake import Snake
from src.domain.board import Board
from src.domain.coordinate import Coordinate


@pytest.mark.parametrize("current_location,board,expected_board", [
    ([Coordinate(x=2, y=2)], Board(width=5, height=5),
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', 'O', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([Coordinate(x=0, y=0)], Board(width=5, height=5),
        [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['O', '', '', '', '']
    ]
    ),
    ([Coordinate(x=0, y=4)], Board(width=5, height=5),
        [
            ['O', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
    ]
    ),
    ([Coordinate(x=3, y=4)], Board(width=5, height=5),
     [
        ['', '', '', 'O', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ]
    ),
    ([Coordinate(x=0, y=0)], Board(width=1, height=1),
     [
        ['O']
    ]
    ),
    ([Coordinate(x=2, y=2)], Board(width=3, height=3),
     [
        ['', '', 'O'],
        ['', '', ''],
        ['', '', '']
    ]
    ),
    ([Coordinate(x=0, y=0), Coordinate(x=1, y=1), Coordinate(x=2, y=2)],
     Board(width=3, height=3),
     [
        ['', '', '='],
        ['', '=', ''],
        ['O', '', '']
    ]
    ),
    ([Coordinate(x=1, y=0), Coordinate(x=1, y=1), Coordinate(x=2, y=1), Coordinate(x=3, y=1)],
     Board(width=4, height=4),
     [
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '=', '=', '='],
        ['', 'O', '', ''],
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
