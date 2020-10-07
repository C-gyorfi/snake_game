class ShowBoard:
    @staticmethod
    def execute(_board, snake):
        board = [
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', '']
        ]

        for i, row in enumerate(board):
            if snake.current_location[0][1] == (len(board) - i) - 1:
                row[snake.current_location[0][0]] = 'O'

        return board
