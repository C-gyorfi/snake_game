import time
import curses
from src.domain.snake import Snake
from src.domain.board import Board
from src.domain.coordinate import Coordinate
from src.use_case.move_snake import MoveSnake
from src.use_case.turn_snake import TurnSnake
from src.use_case.show_board import ShowBoard

# Init game objects
board = Board(width=10, height=10)
snake = Snake([Coordinate(x=0, y=0), Coordinate(
    x=1, y=0), Coordinate(x=2, y=0)], 'N')
food = [Coordinate(x=5, y=5)]
move_snake = MoveSnake()
show_board = ShowBoard()
turn_snake = TurnSnake()

# initialize application
stdscr = curses.initscr()
# get non-blocking user input
stdscr.timeout(100)

# tweak terminal settings
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

# get user input for direction


def getDirection():
    key = stdscr.getch()
    if key == curses.KEY_RIGHT:
        return 'E'
    elif key == curses.KEY_LEFT:
        return 'W'
    elif key == curses.KEY_DOWN:
        return 'S'
    elif key == curses.KEY_UP:
        return 'N'
    else:
        return None


game_over = False
while not game_over:
    for i, row in enumerate(show_board.execute(board, snake, food)):
        current_row = ' '.join(row)
        stdscr.addstr(i, 10, current_row)
    # update the screen
    stdscr.refresh()
    # wait for a bit
    time.sleep(0.1)
    direction = getDirection()
    turn_snake.execute(direction, snake)
    move_snake.execute(board, snake, food)

stdscr.clear()

# reverse terminal settings
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

# close the application
curses.endwin()
