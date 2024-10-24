from Entity import Entity
import random

class Player(Entity):

    def __init__(self, age, Health):
        super().__init__("Bob", 20, 20, "jsp", 1, 5)
        self.age = age
        self.Health = Health
        self.inventory = []

    def attack(self, EnemyHealth):
        miss_chance = 0

        if self.level <= 5:
            miss_chance = 40
        elif self.level <= 10:
            miss_chance = 30
        elif self.level <= 15:
            miss_chance = 20
        elif self.level <= 20:
            miss_chance = 10
        elif self.level <= 25:
            miss_chance = 0

        roll = random.randint(1, 100)

        if roll > miss_chance:
            EnemyHealth -= self.strength
        else:
            print("L'attaque a échoué!")

        return EnemyHealth

    def levelup(self):
        self.level += 1
        self.Health += 10 + (self.level * 1.25)
        self.maxHealth += 10 + (self.level * 1.25)
        self.age += 1
        self.strength += 10 + (self.level * 1.20)

    def addOjbect(self, Objet):
        if Objet == "":
            print("Vous ne pouvez pas ajouter rien")
        else:
            self.inventory.append(Objet)
            print(f"{Objet}Est ajouter dans votre inventaire")

    def removeOjbect(self, Objet):
        if Objet == "":
            print("Vous ne pouvez pas supprimer rien")
        else:
            self.inventory.remove(Objet)
            print(f"{Objet}Est supprimer rien")