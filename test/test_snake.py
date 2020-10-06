from assertpy import assert_that
from src.domain.snake import Snake

def test_snake_can_be_initialised_with_a_starting_location():
    expeteced_snake_coordinates = [[0, 1], [0, 0]]
    snake = Snake(expeteced_snake_coordinates, 'S')
    assert_that(snake.location()).is_equal_to(expeteced_snake_coordinates)

def test_snake_can_be_initialised_with_a_heading():
    expeteced_heading = 'N'
    snake = Snake([[0,0]], expeteced_heading)
    assert_that(snake.head()).is_equal_to(expeteced_heading)
