from map import Map 

class Position:

    def __init__(self, map_instance):
        self.map_instance = map_instance

    def afficher_position(self):
        print("\n Ou voulez vous aller ? ")
        print("1. Up")
        print("2. Down")
        print("3. Left")
        print("4. Right")

        reponce = input("> ")

        if reponce == "1":
            self.map_instance.player_y  -= 1
            print("le joueur a bouger ")
        if reponce == "2":
            self.map_instance.player_y   += 1
        if reponce == "3":
            self.map_instance.player_x -= 1
        if reponce == "4":
           self.map_instance.player_x  += 1


    # def Move(self, direction):
        
    #     if direction == "Up":
    #         self.y -= 1
    #     if direction == "Down":
    #         self.y += 1
    #     if direction == "Left":
    #         self.x -= 1
    #     if direction == "Right":
    #         self.x += 1