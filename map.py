class Map:
    def __init__(self):
        self.map = [
            [2, 2 ,2 ,2, 2, 2, 2, 2, 2, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 0 ,0 ,0, 0, 0, 0, 0, 0, 2],
            [2, 2 ,2 ,2, 2, 2, 2, 2, 2, 2],
        ]   
        self.player_x = 2
        self.player_y = 2
    def afficher_map(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.player_x == x and self.player_y == y:
                    print("P", end=" ")  
                elif self.map[y][x] == 2:
                    print("#", end=" ") 
                else:
                    print(" ", end=" ")  
            print() 
    