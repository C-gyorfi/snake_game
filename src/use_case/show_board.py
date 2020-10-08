class ShowBoard:
    EMPTY_TILE = ''
    HEAD = 'O'
    BODY = '='

    @staticmethod
    def execute(board, snake):
        drawn_board = ShowBoard.draw_board(board)
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
            y_coordinate_of_row = (len(board) - i) - 1
            for j, coordinate in enumerate(snake.current_location):
                if coordinate[1] == y_coordinate_of_row:
                    row[coordinate[0]] = ShowBoard.HEAD if j == 0 else ShowBoard.BODY
        return board
