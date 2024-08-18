from dataclasses import dataclass


@dataclass
class Vector2D:
    """
    Supports addition, subtraction, negation and scalar multiplication for some basic vector operations
    """
    x: float = 0
    y: float = 0

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, other):
        return Vector2D(other * self.x, other * self.y)

    def __rmul__(self, other):
        return self * other


if __name__ == "__main__":
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)

    v3 = v1 + v2  # Vector addition
    print(v3)  # Output: Vector2D(x=4, y=6)

    v4 = v2 - v1  # Vector subtraction
    print(v4)  # Output: Vector2D(x=2, y=2)

    v5 = -v1  # Negation
    print(v5)  # Output: Vector2D(x=-1, y=-2)

    v6 = 3 * v1  # Scalar multiplication
    print(v6)  # Output: Vector2D(x=3, y=6)
