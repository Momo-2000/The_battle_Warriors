import importlib


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.attack = 7
        self.health = 50


def fight(unit_1, unit_2):
    while 1:
        unit_2.health = unit_2.health - unit_1.attack
        if unit_2.health <= 0:
            return True
        unit_1.health = unit_1.health - unit_2.attack
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


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

assert fight(chuck, bruce) == True
assert fight(dave, carl) == False
assert chuck.is_alive == True
assert bruce.is_alive == False
assert carl.is_alive == True
assert dave.is_alive == False
assert fight(carl, mark) == False
assert carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

assert battle.fight(my_army, enemy_army) == True
assert battle.fight(army_3, army_4) == False
