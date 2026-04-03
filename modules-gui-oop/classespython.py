class Player:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    
    def attack(self):
        print(f'{self.name} attacks with {self.hp} HP!')

    def level_up(self):
        self.level += 1
        print(f'{self.name} leveled up! Current level: {self.level}')

hero = Player("Peter", 100, 1)

hero.attack()
hero.level_up()