import game_functions

if __name__ == "__main__":
    game_functions.init_players(2)
    board = game_functions.init_board(3,3)
    game_functions.display_board(board)
