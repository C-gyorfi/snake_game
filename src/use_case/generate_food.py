import random
from src.domain.coordinate import Coordinate


class GenerateFood:
    @staticmethod
    def execute(board: object, snake: object, food: object):
        if not food:
            possible_food_coordinates = []
            for y in range(board.height):
                for x in range(board.width):
                    possible_food_coordinates.append([x, y])
            for coordinate in snake.current_location:
                possible_food_coordinates.remove([coordinate.x, coordinate.y])
            random_coordinate = random.choice(possible_food_coordinates)
            food.append(
                Coordinate(
                    x=random_coordinate[0],
                    y=random_coordinate[1]))
