import importlib


class Warrior:
    def __init__(self):
        self.health = 50
        self.defense = 0
        self.attack = 5
        self.vampirism = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.attack = 7
        self.defense = 0
        self.health = 50
        self.vampirism = 0


class Defender(Warrior):
    def __init__(self):
        self.attack = 3
        self.health = 60
        self.defense = 2
        self.vampirism = 0


class Vampire(Warrior):
    def __init__(self):
        self.attack = 4
        self.health = 40
        self.defense = 0
        self.vampirism = 0.5


def fight(unit_1, unit_2):
    while 1:
        if unit_1.attack > unit_2.defense:  # 判断 防御值 ----
            unit_2.health = unit_2.health - unit_1.attack + unit_2.defense  # 造成伤害
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.defense) * unit_1.vampirism  # 吸血
        if unit_2.health <= 0:
            return True
        if unit_2.attack > unit_1.defense:  # 判断 防御值 ----
            unit_1.health = unit_1.health - unit_2.attack + unit_1.defense  # 造成伤害
            unit_2.health = unit_2.health + (unit_2.attack - unit_1.defense) * unit_2.vampirism  # 吸血
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.ar = []

    def add_units(self, type, num):
        for i in range(0, num):
            obj = type()
            self.ar.append(obj)


class Battle:
    def fight(self, unit_1, unit_2):
        # assert isinstance(unit_1, Army)
        while 1:
            if fight(unit_1.ar[0], unit_2.ar[0]):
                del (unit_2.ar[0])
                if len(unit_2.ar) == 0:
                    return True
            else:
                del (unit_1.ar[0])
                if len(unit_1.ar) == 0:
                    return False


# 以下代码将核查Python代码的正确性
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()

assert fight(chuck, bruce) == True
assert fight(dave, carl) == False
assert chuck.is_alive == True
assert bruce.is_alive == False
assert carl.is_alive == True
assert dave.is_alive == False
assert fight(carl, mark) == False
assert carl.is_alive == False
assert fight(bob, mike) == False
assert fight(lancelot, rog) == True
assert fight(eric, richard) == False
assert fight(ogre, adam) == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

assert battle.fight(my_army, enemy_army) == False
assert battle.fight(army_3, army_4) == True
