# simple_game_engine

## Methods for Game
```python
from abc import ABC, abstractmethod

from src.core.cell import Cell
from src.core.color import Color
from src.core.game_engine import GameEngine


class Game(ABC):
    @abstractmethod
    def initialize(self):
        pass

    def set_title(self, title: str):
       pass

    def set_screen_size(self, width: int, height: int):
        pass

    def show_grid(self, flag: bool):
        pass

    def show_message(self, text: str):
        pass

    def set_cell(self, x: int, y: int, color=None, text=None):
        pass

    def get_cell_color(self, x: int, y: int) -> Color:
        pass

    def get_cell_text(self, x: int, y: int) -> str:
        pass

    def set_turn_timer(self, interval_ms: int):
        pass

    def stop_turn_timer(self):
        pass

    def on_turn(self, step: int):
        """
        :param step: step counting starts from one
        :return: None
        """

    def on_left_click(self, x: int, y: int):
        pass

    def on_right_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass
```

## TicTacToeGame
![Иллюстрация к проекту](https://github.com/Yolshin195/simple_game_engine/blob/main/source/ticTacToeGame.png)

```python
from src.core.game import Game


class TicTacToeGame(Game):
    def initialize(self):
        self.title = "Tic Tac Toe!"
        self.set_screen_size(3, 3)

    def on_mouse_click(self, x: int, y: int):
        self.set_cell(x, y, text="X")

    def on_key_press(self, char: str, keycode: int):
        if 49 <= keycode <= 57:
            self.set_cell_by_index(int(char) - 1, text="X")
```