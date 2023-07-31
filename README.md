# simple_game_engine

## Methods for Game
```python
class Game:
    def initialize(self):
        pass
    
    def set_screen_size(self, width: int, height: int):
        pass
    
    def show_grid(self, flag: bool):
        pass

    def set_cell(self, x: int, y: int, color=None, text=None):
        pass

    def get_cell(self, x: int, y: int):
        pass
    
    def set_turn_timer(self, call_interval: int):
        pass
    
    def stop_turn_timer(self):
        pass
    
    def on_turn(self, step: int):
        pass

    def on_mouse_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass

    def on_key_release(self, char: str, keycode: int):
        pass

    def show_message_dialog(self, cell_color, message, text_color, text_size):
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