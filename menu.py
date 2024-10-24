import os


class Menu:
    def afficher_menu(self):
        print(" _______ Menu du jeu _______")
        print("1. Créer une nouvelle partie")
        print("2. Charger la partie")
        print("3. About")
        print("4. Quitter")
        
        reponse = input("> ")
        
        os.system("cls") # pour clear le terminal

        if reponse == "1":
            print("Création de la partie")
            Nom = input("Nom du joueur : ")
            os.system("cls")
        elif reponse == "2":
            print("Chargement de la partie")
        elif reponse == "3":
            print("À propos")
        elif reponse == "4":
            print("Quitter")
        else:
            print("Option non valide")


