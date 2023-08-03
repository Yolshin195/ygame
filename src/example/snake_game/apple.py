from src.core.color import RED
from src.example.snake_game.point import Point


class Apple(Point):
    def __init__(self, x, y):
        super().__init__(x, y, "\U0001F34E", RED)
