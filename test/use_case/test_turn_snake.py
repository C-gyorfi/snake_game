from assertpy import assert_that
from src.use_case.turn_snake import TurnSnake
from src.domain.snake import Snake


def test_can_turn_the_snake_north_when_facing_east():
    current_location = 'Dummy'
    current_heading = 'E'
    snake = Snake('Dummy', current_heading)

    TurnSnake().execute('N', snake)
    assert_that(snake.current_heading).is_equal_to('N')


def test_can_turn_the_snake_south_when_facing_east():
    current_heading = 'E'
    snake = Snake('Dummy', current_heading)

    TurnSnake().execute('S', snake)
    assert_that(snake.current_heading).is_equal_to('S')


def test_can_turn_the_snake_west_when_facing_north():
    current_heading = 'N'
    snake = Snake('Dummy', current_heading)

    TurnSnake().execute('W', snake)
    assert_that(snake.current_heading).is_equal_to('W')


def test_cannot_turn_the_snake_west_when_facing_east():
    current_heading = 'E'
    snake = Snake('Dummy', current_heading)

    TurnSnake().execute('W', snake)
    assert_that(snake.current_heading).is_equal_to('E')


def test_can_turn_the_snake_south_when_facing_west():
    current_heading = 'W'
    snake = Snake('Dummy', current_heading)

    TurnSnake().execute('S', snake)
    assert_that(snake.current_heading).is_equal_to('S')
