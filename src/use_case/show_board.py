class ShowBoard:
    EMPTY_TILE = ' '
    HEAD = '■'
    BODY = '◙'
    FRUITS = ['🍇 ', '🍉', '🍊', '🍌', '🍍 ', '🥭 ', '🍎 ', '🍓']

    @staticmethod
    def execute(board, snake, food=None):
        drawn_board = ShowBoard.draw_board(board)
        drawn_board = ShowBoard.draw_food_on_board(drawn_board, food)
        drawn_board = ShowBoard.draw_snake_on_board(drawn_board, snake)
        return drawn_board

    @staticmethod
    def draw_board(board):
        drawn_board = []
        for _n in range(board.height):
            row = []
            for _n in range(board.width):
                row.append(ShowBoard.EMPTY_TILE)
            drawn_board.append(row)
        return drawn_board

    @staticmethod
    def draw_snake_on_board(board, snake):
        for i, row in enumerate(board):
            y_coordinate_of_board = (len(board) - i) - 1
            for j, coordinate in enumerate(snake.current_location):
                if coordinate.y == y_coordinate_of_board:
                    row[coordinate.x] = ShowBoard.HEAD if j == 0 else ShowBoard.BODY
        return board

    @staticmethod
    def draw_food_on_board(board, food):
        if food is None:
            return board
        else:
            for i, row in enumerate(board):
                y_coordinate_of_board = (len(board) - i) - 1
                for j, coordinate in enumerate(food):
                    if coordinate.y == y_coordinate_of_board:
                        row[coordinate.x] = ShowBoard.FRUITS[0]
        return board
