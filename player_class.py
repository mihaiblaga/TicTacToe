class Player():
    """
    Basic Class Object
    """

    def __init__(self, number):
        self.number = number
        self.name = ""
        self.p_input = ""
        self.coord = []
    
    def get_player_name(self):
        self.name = input()
    
    def player_move(self):
        # de incercat try statement
        print(f"It is {self.name}'s turn")
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
        return self.coord

if __name__ == "__main__":
    player = Player(1)
    player.get_player_name()
    player.player_move()