import time
import curses
import random
from src.domain.snake import Snake
from src.use_case.move_snake import MoveSnake
from src.use_case.turn_snake import TurnSnake
from src.use_case.show_board import ShowBoard
from src.domain.board import Board
from src.domain.coordinate import Coordinate

# Init game objects
board = Board(width=10, height=10)
snake = Snake([Coordinate(x=0, y=0), Coordinate(x=1, y=0), Coordinate(x=2, y=0)], 'N')
move_snake = MoveSnake()
show_board = ShowBoard()
turn_snake = TurnSnake()

# initialize application
stdscr = curses.initscr()

# tweak terminal settings
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

game_over = False
while 1:
  for i, row in enumerate(show_board.execute(board, snake)):
    current_row = ' '.join(row)
    stdscr.addstr(i, 10, current_row)
  # update the screen
  stdscr.refresh()
  # wait for a bit
  time.sleep(0.3)
  turn_snake.execute(random.choice(['N', 'E', 'S', 'W']), snake)
  move_snake.execute(board, snake)

stdscr.clear()

# reverse terminal settings
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

# close the application
curses.endwin()