class Entity:

    def __init__(self, name, health, maxHealth,  weapon, level, strength):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.weapon = weapon
        self.level = level
        self.strength = strength
        self.inventory = []

    def attack(self, EnemyHealth):
        pass
