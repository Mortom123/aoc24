from utils.point import Point
from enum import Enum

class Direction(Enum):
    UP = 1
    NORTH = 1

    DOWN = 2
    SOUTH = 2

    LEFT = 3
    WEST = 3

    RIGHT = 4
    EAST = 4

    def right(self):
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP

    def left(self):
        match self:
            case Direction.UP:
                return Direction.LEFT
            case Direction.RIGHT:
                return Direction.UP
            case Direction.DOWN:
                return Direction.RIGHT
            case Direction.LEFT:
                return Direction.DOWN

    def inverse(self):
        match self:
            case Direction.UP:
                return Direction.DOWN
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT

    def point(self):
        match self:
            case Direction.UP:
                return Point(0, 1)
            case Direction.RIGHT:
                return Point(1, 0)
            case Direction.DOWN:
                return Point(0, -1)
            case Direction.LEFT:
                return Point(-1, 0)

if __name__ == "__main__":
    print(Direction.UP, Direction.NORTH)

