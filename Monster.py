from Entity import Entity
import random

class Monster(Entity):

    def __init__(self, health, level):
        super().__init__("Bob", 50, "Epée", level, 10)
        self.health = health
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