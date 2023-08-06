from ygame.example.calculator_game.calculator_game import CalculatorGame
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(CalculatorGame()).initialize()


if __name__ == "__main__":
    main()