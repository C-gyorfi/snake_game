class EndGame:
    @staticmethod
    def execute(snake: object):
        dedup = []
        for coordinate in snake.current_location:
            dedup.append((coordinate.x, coordinate.y))
        return len(snake.current_location) > len(set(dedup))
