from assertpy import assert_that
from src.domain.snake import Snake
from src.use_case.move_snake import MoveSnake
from src.use_case.turn_snake import TurnSnake
from src.use_case.show_board import ShowBoard
from src.use_case.generate_food import GenerateFood
from src.use_case.end_game import EndGame
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


def test_snake_can_grow_when_feeding():
    board = Board(width=4, height=4)
    snake = Snake(
        [
            Coordinate(x=0, y=0),
            Coordinate(x=3, y=0),
        ],
        'E'
    )
    food = [Coordinate(x=1, y=0)]

    rendered_board = ShowBoard.execute(board, snake, food)
    assert_that(rendered_board[3][0]).is_equal_to('■')
    assert_that(ShowBoard.FRUITS).contains(rendered_board[3][1])
    assert_that(rendered_board[3][2]).is_equal_to(' ')
    assert_that(rendered_board[3][3]).is_equal_to('◙')
    assert_that(len(snake.current_location)).is_equal_to(2)

    MoveSnake().execute(board, snake, food)
    rendered_board = ShowBoard.execute(board, snake, food)
    assert_that(rendered_board[3][0]).is_equal_to('◙')
    assert_that(rendered_board[3][1]).is_equal_to('■')
    assert_that(rendered_board[3][2]).is_equal_to(' ')
    assert_that(rendered_board[3][3]).is_equal_to('◙')
    assert_that(food).is_empty()
    assert_that(len(snake.current_location)).is_equal_to(3)


def test_can_generate_food():
    board = Board(width=4, height=4)
    snake_coordinates = [[0, 0], [3, 0]]
    possible_food_coordinates = [
        [1, 0], [2, 0],
        [0, 1], [1, 1], [2, 1], [3, 1],
        [0, 2], [1, 2], [2, 2], [3, 2],
        [0, 3], [1, 3], [2, 3], [3, 3]
    ]
    snake = Snake(
        [
            Coordinate(x=snake_coordinates[0][0], y=snake_coordinates[0][1]),
            Coordinate(x=snake_coordinates[1][0], y=snake_coordinates[1][1]),
        ],
        'E'
    )
    food = []

    GenerateFood().execute(board=board, snake=snake, food=food)

    assert_that(food).is_not_empty()
    for food_coordinate in [[food[0].x, food[0].y]]:
        assert_that(possible_food_coordinates).contains(food_coordinate)
        assert_that(snake_coordinates).does_not_contain(food_coordinate)


def test_can_end_game():
    snake = Snake(
        [
            Coordinate(x=0, y=0),
            Coordinate(x=3, y=0),
        ],
        'E'
    )
    assert_that(EndGame.execute(snake)).is_false()

    dead_snake = Snake(
        [
            Coordinate(x=0, y=0),
            Coordinate(x=3, y=0),
            Coordinate(x=0, y=0),
        ],
        'E'
    )
    assert_that(EndGame.execute(dead_snake)).is_true()
