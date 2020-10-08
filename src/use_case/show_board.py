class ShowBoard:
    @staticmethod
    def execute(board_size, snake):
        board = []
        for height in range(board_size[1]):
            row = []
            for width in range(board_size[0]):
                row.append('')
            board.append(row)

        for i, row in enumerate(board):
            if snake.current_location[0][1] == (len(board) - i) - 1:
                row[snake.current_location[0][0]] = 'O'

        return board
