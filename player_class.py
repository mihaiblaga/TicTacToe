class Player():
    """
    Basic Class Object
    """

    def __init__(self, number):
        self.number = number
        self.attr = ""
        self.name = ""
        self.p_input = ""
        self.coord = []
    
    def get_player_name(self):
        if self.number == 1:
            self.attr = "first"
        else:
            self.attr = "second"
        print("Insert {} player name here: ".format(self.attr))
        self.name = input()
    
    def player_move(self):
        # de incercat try statement

        print("Input x coord")
        self.p_input = int(input())
        if  isinstance(self.p_input,int):
            self.coord.append(self.p_input)
        else:
            print("Input is not an integer")
        
        print("Input y coord")
        self.p_input = int(input())
        if  isinstance(self.p_input,int):
            self.coord.append(self.p_input)
        else:
            print("Input is not an integer")
        print(self.coord)

if __name__ == "__main__":
    player = Player(1)
    player.player_move()