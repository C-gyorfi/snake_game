from assertpy import assert_that
from src.domain.coordinate import Coordinate


def test_coordinate_can_have_an_x_and_y_param():
    point = Coordinate(x=3, y=5)
    assert_that(point.x).is_equal_to(3)
    assert_that(point.y).is_equal_to(5)

