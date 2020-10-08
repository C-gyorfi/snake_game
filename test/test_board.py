from assertpy import assert_that
from src.domain.board import Board


def test_board_can_have_a_width_and_height():
    board = Board(width=3, height=5)
    assert_that(board.width).is_equal_to(3)
    assert_that(board.height).is_equal_to(5)
