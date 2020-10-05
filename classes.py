class Player():
    """
    Basic Class Object
    """


    def __init__(self, number):
        self.number = number
        self.attr = ""
        self.name = ""
    
    def get_player_name(self):
        if self.number == 1:
            self.attr = "First"
        else:
            self.attr = "Second"
        print("Insert {} player name here: ".format(self.attr))
        self.name = input()




class Board():
    """
    Basic Board Object
    """
    def __init__(self):

        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def display_board(self):
        for row in self.board:
            print(row)

    def change_board(self,x,y,player):
        if player == 1:
            self.board[x][y] = "X"
        else:
            self.board[x][y] = "O"
    



# brd = Board()
# brd.display_board()
# brd.change_board(1,1,1)
# brd.display_board()
player = Player(1)
player.get_player_name()
print(player.name)