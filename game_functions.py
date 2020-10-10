from player_class import Player

def init_board(rows,cols):
    board = [[0 for i in range(rows)] for j in range(cols) ]
    # board = [['O', 'O', 'O'], 
    #          ['O', 'O', 'O'], 
    #          ['O', 'O', 'O']]
    return board

def display_board(board):
    for row in board:
        print(row)

def change_board(coord,player_number,board):
    if board[coord[0]][coord[1]] == 0:
        if player_number == 0:
            board[coord[0]][coord[1]] = "X"
        elif player_number == 1:
            board[coord[0]][coord[1]] = "O"
    else:
        print("Invalid location")

def init_players(player_number):
    player_list = []
    for i in range(player_number):
        player_list.append(Player(i))
    for i, player in enumerate(player_list):
        print(f"Insert name for player {i + 1}:")
        player.get_player_name()
    return player_list

def check_equal(lst):
    return len(set(lst)) <= 1 and lst != [0,0,0]

def do_player_turn(players,pnumber):
    players[pnumber-1].player_move()

def get_column(array, i):
    return [row[i] for row in array]

def check_board(board):

    if check_equal(board[0][:]):
        return False
    if check_equal(board[1][:]):
        return False
    if check_equal(board[2][:]):
        return False
    if check_equal([col[0] for col in board]):
        return False
    if check_equal([col[1] for col in board]):
        return False
    if check_equal([col[2] for col in board]):
        return False
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return False
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return False

    return True