from typing import Optional
from dataclasses import dataclass
import numpy as np

@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def np(self):
        return np.asarray([self.x, self.y])

@dataclass(unsafe_hash=True)
class InplacePoint:
    x: int
    y: int

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def np(self):
        return np.asarray([self.x, self.y])

def get_neighbors(point: np.ndarray, directions: Optional[np.ndarray] = None) -> np.ndarray:
    if directions is None:
        directions = np.asarray([
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ])
    return point + directions

if __name__ == "__main__":
    print(get_neighbors(np.asarray([0,0])))