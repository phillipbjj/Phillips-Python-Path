class Pokemon:
    def __init__(self, name, hp, attack, defense, sp_attack, sp_defense, speed, total):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.total = total
    def __repr__(self):
        return f'{self.name} has HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Sp. Attack: {self.sp_attack}, Sp. Defense: {self.sp_defense}, Speed: {self.speed}, Total EVs: {self.total}'
    
