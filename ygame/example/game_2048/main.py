# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.example.game_2048.game_2048 import Game2048
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(Game2048()).initialize()


if __name__ == "__main__":
    main()
