from src.example.tic_tac_toe_game.tic_tac_toe_game import TicTacToeGame
from src.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(TicTacToeGame()).initialize()


if __name__ == "__main__":
    main()