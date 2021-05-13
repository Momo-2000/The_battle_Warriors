import importlib


class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.attack = 5
        self.vampirism = 0
        self.through = 0
        self.heals = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.max_health = 50
        self.attack = 7
        self.defense = 0
        self.health = 50
        self.vampirism = 0
        self.through = 0
        self.heals = 0


class Defender(Warrior):
    def __init__(self):
        self.max_health = 60
        self.attack = 3
        self.health = 60
        self.defense = 2
        self.vampirism = 0
        self.through = 0
        self.heals = 0


class Vampire(Warrior):
    def __init__(self):
        self.max_health = 40
        self.attack = 4
        self.health = 40
        self.defense = 0
        self.vampirism = 0.5
        self.through = 0
        self.heals = 0


class Lancer(Warrior):
    def __init__(self):
        self.attack = 6
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.through = 0.5
        self.heals = 0


class Healer():
    def __init__(self):
        self.attack = 0
        self.health = 60
        self.defense = 0
        self.vampirism = 0
        self.through = 0
        self.heals = 2

    def heal(self, rapist):
        rapist.health = rapist.health + self.heals
        if rapist.health > rapist.max_health:
            rapist.health = rapist.max_health


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
            if unit_1.ar[0].attack > unit_2.ar[0].defense:  # 判断 防御值 ----
                unit_2.ar[0].health = unit_2.ar[0].health - unit_1.ar[0].attack + unit_2.ar[0].defense  # 造成伤害
                unit_1.ar[0].health = unit_1.ar[0].health + (unit_1.ar[0].attack - unit_2.ar[0].defense) * unit_1.ar[
                    0].vampirism  # 吸血
            if len(unit_2.ar) > 1:  # 判断穿透
                unit_2.ar[1].health = unit_2.ar[1].health - unit_1.ar[0].attack * unit_1.ar[0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_2.ar)):
                if unit_2.ar[i].health > 0:
                    temp.append(unit_2.ar[i])
            unit_2.ar = temp
            for i in range(0, len(unit_2.ar)):
                if i != 0:
                    if unit_2.ar[i].heals > 0:
                        unit_2.ar[i].heal(unit_2.ar[i - 1])

            if len(unit_2.ar) == 0:
                return True

            if unit_2.ar[0].attack > unit_1.ar[0].defense:  # 判断 防御值 ----
                unit_1.ar[0].health = unit_1.ar[0].health - unit_2.ar[0].attack + unit_1.ar[0].defense  # 造成伤害
                unit_2.ar[0].health = unit_2.ar[0].health + (unit_2.ar[0].attack - unit_1.ar[0].defense) * unit_2.ar[
                    0].vampirism  # 吸血
            if len(unit_1.ar) > 1:  # 判断穿透
                unit_1.ar[1].health = unit_1.ar[1].health - unit_2.ar[0].attack * unit_2.ar[0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_1.ar)):
                if unit_1.ar[i].health > 0:
                    temp.append(unit_1.ar[i])
            unit_1.ar = temp
            for i in range(0, len(unit_1.ar)):
                if i != 0:
                    if unit_1.ar[i].heals > 0:
                        unit_1.ar[i].heal(unit_1.ar[i - 1])
            if len(unit_1.ar) == 0:
                return False

    def straight_fight(self, unit_1, unit_2):
        while 1:
            temp1 = []
            temp2 = []
            if len(unit_1.ar) > len(unit_2.ar):
                for i in range(0,len(unit_2.ar)):
                    if fight(unit_1.ar[i],unit_2.ar[i]) :
                        temp1.append(unit_1.ar[i])
                    else :
                        temp2.append(unit_2.ar[i])
                for i in range(len(unit_2.ar),len(unit_1.ar)):
                    temp1.append(unit_1.ar[i])
            if len(unit_2.ar) > len(unit_1.ar):
                for i in range(0,len(unit_1.ar)):
                    if fight(unit_1.ar[i],unit_2.ar[i]) :
                        temp1.append(unit_1.ar[i])
                    else :
                        temp2.append(unit_2.ar[i])
                for i in range(len(unit_1.ar),len(unit_2.ar)):
                    temp1.append(unit_2.ar[i])
            unit_1.ar = temp1
            unit_2.ar = temp2
            if len(unit_1.ar) == 0:
                return True
            if len(unit_2.ar) == 0:
                return False


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
freelancer = Lancer()
vampire = Vampire()
priest = Healer()

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
assert fight(freelancer, vampire) == True
assert freelancer.is_alive == True
assert freelancer.health == 14
priest.heal(freelancer)
assert freelancer.health == 16

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 4)
enemy_army.add_units(Healer, 1)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)
enemy_army.add_units(Healer, 1)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Healer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Healer, 1)
army_4.add_units(Lancer, 2)

army_5 = Army()
army_5.add_units(Warrior, 10)

army_6 = Army()
army_6.add_units(Warrior, 6)
army_6.add_units(Lancer, 5)

battle = Battle()

assert battle.fight(my_army, enemy_army) == False
assert battle.fight(army_3, army_4) == False
assert battle.straight_fight(army_5, army_6) == False
