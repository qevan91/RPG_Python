class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Move(self, direction):
        if direction == "Up":
            self.y -= 1
        if direction == "Down":
            self.y += 1
        if direction == "Left":
            self.x -= 1
        if direction == "Right":
            self.x += 1