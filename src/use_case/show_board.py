class ShowBoard:
    @staticmethod
    def execute(board, snake):
        drawn_board = []
        for _n in range(board.height):
            row = []
            for _n in range(board.width):
                row.append('')
            drawn_board.append(row)

        for i, row in enumerate(drawn_board):
            if snake.current_location[0][1] == (len(drawn_board) - i) - 1:
                row[snake.current_location[0][0]] = 'O'

        return drawn_board
