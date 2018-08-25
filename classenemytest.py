class Enemy(object):
    pass


class Player(object):

    def __init__(self,HP,ATK):
        self.HP = 100
        self.ATK = 10
  
    def actions(self,DMG):
        self.actions = [
                'Sword Slash',
                'Dodge',
                ]


class Goblin(Enemy):

    def __init__(self,HP,ATK):
        self.HP = 25
        self.ATK = 5
        if HP =< 0:
            print("Arrrght!")



x = Goblin()


