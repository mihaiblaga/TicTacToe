from player_class import Player

def init_board(rows,cols):
    board = [["0" for i in range(rows)] for j in range(cols) ]
    return board

def display_board(board):
    for row in board:
        print(row)

def change_board(x,y,player_number,board):
    if player_number == 1 and board[x][y] == 0:
        board[x][y] = "X"
    elif board[x][y] == 0:
        board[x][y] = "O"

def init_players(player_number):
    player_list = []
    for i in range(player_number):
        player_list.append(Player(i))
    for player in player_list:
        print(f"Insert name for player {player}:")
        player.get_player_name()


