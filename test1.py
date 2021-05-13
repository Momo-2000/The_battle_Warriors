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


# 以下代码将核查Python代码的正确性
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
print(fight(chuck, bruce))
assert fight(chuck, bruce) == True, "chuck vs. bruce"
assert fight(dave, carl) == False, "dave vs. carl"
assert chuck.is_alive == True, "chuck should be alive"
assert bruce.is_alive == False, "chuck should NOT be alive"
assert carl.is_alive == True, "carl should be alive"
assert dave.is_alive == False, "dave should NOT be alive"
