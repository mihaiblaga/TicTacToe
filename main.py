import game_functions

if __name__ == "__main__":

    running = True
    players_list = game_functions.init_players(2)
    board = game_functions.init_board(3,3)
    game_functions.display_board(board)
    # game_functions.display_board(board)
    # game_functions.do_player_turn(players_list)

    while running:
        #Take input
        game_functions.do_player_turn(players_list,1)

        #Do the move
        game_functions.change_board(players_list[0].coord,players_list[0].number,board)
        
        #Display board
        game_functions.display_board(board)

        #Check the board
        running = game_functions.check_board(board)

        #Take input
        game_functions.do_player_turn(players_list,2)

        #Do the move
        game_functions.change_board(players_list[1].coord,players_list[1].number,board)

        #Display board
        game_functions.display_board(board)

        #Check the board
        running = game_functions.check_board(board)
    
