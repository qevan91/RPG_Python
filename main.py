import os
from menu import Menu
from map import Map 
from position import Position


menu = Menu()
menu.afficher_menu()
ma_carte = Map()
player_position = Position(ma_carte)  
while True:
    os.system("cls")
    ma_carte.afficher_map()  
    player_position.afficher_position() 
