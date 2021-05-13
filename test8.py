import importlib


class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.attack = 5
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0

    @property
    def is_alive(self):
        return self.health > 0
    def equip_weapon(self,weapon):
        self.health=self.health+weapon.health
        self.max_health=self.max_health+weapon.health
        if self.attack!=0:
            self.attack=self.attack+weapon.attack
            if self.attack<0:
                self.attack=0
        if self.defense!=0:
            self.defense=self.defense+weapon.defense
            if self.defense<0:
                self.defense=0
        if self.vampirism!=0:
            self.vampirism=self.vampirism+weapon.vampirism
            if self.vampirism<0:
                self.vampirism=0
        if self.heal_power!=0:
            self.heal_power= self.heal_power + weapon.heal_power
            if self.heal_power<0:
                self.heal_power=0




class Knight(Warrior):
    def __init__(self):
        self.max_health = 50
        self.attack = 7
        self.defense = 0
        self.health = 50
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0


class Defender(Warrior):
    def __init__(self):
        self.max_health = 60
        self.attack = 3
        self.health = 60
        self.defense = 2
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0


class Vampire(Warrior):
    def __init__(self):
        self.max_health = 40
        self.attack = 4
        self.health = 40
        self.defense = 0
        self.vampirism = 50
        self.through = 0
        self.heal_power = 0


class Lancer(Warrior):
    def __init__(self):
        self.attack = 6
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.through = 0.5
        self.heal_power = 0


class Healer(Warrior):
    def __init__(self):
        self.attack = 0
        self.health = 60
        self.max_health = 60
        self.defense = 0
        self.vampirism = 0
        self.through = 0
        self.heal_power = 2

    def heal(self, rapist):
        rapist.health = rapist.health + self.heal_power
        if rapist.health > rapist.max_health:
            rapist.health = rapist.max_health


def fight(unit_1, unit_2):
    while 1:
        if unit_1.attack > unit_2.defense:  # 判断 防御值 ----
            unit_2.health = unit_2.health - unit_1.attack + unit_2.defense  # 造成伤害
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.defense) * unit_1.vampirism*0.01  # 吸血
        if unit_2.health <= 0:
            return True
        if unit_2.attack > unit_1.defense:  # 判断 防御值 ----
            unit_1.health = unit_1.health - unit_2.attack + unit_1.defense  # 造成伤害
            unit_2.health = unit_2.health + (unit_2.attack - unit_1.defense) * unit_2.vampirism*0.01  # 吸血
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, type, num):
        for i in range(0, num):
            obj = type()
            self.units.append(obj)


class Battle:
    def fight(self, unit_1, unit_2):
        # assert isinstance(unit_1, Army)
        while 1:
            if unit_1.units[0].attack > unit_2.units[0].defense:  # 判断 防御值 ----
                unit_2.units[0].health = unit_2.units[0].health - unit_1.units[0].attack + unit_2.units[0].defense  # 造成伤害
                unit_1.units[0].health = unit_1.units[0].health + (unit_1.units[0].attack - unit_2.units[0].defense) * unit_1.units[
                    0].vampirism*0.01  # 吸血
                if unit_1.units[0].health>unit_1.units[0].max_health:
                    unit_1.units[0].health=unit_1.units[0].max_health
            if len(unit_2.units) > 1:  # 判断穿透
                unit_2.units[1].health = unit_2.units[1].health - unit_1.units[0].attack * unit_1.units[0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_2.units)):
                if unit_2.units[i].health > 0:
                    temp.append(unit_2.units[i])
            unit_2.units = temp
            for i in range(0, len(unit_2.units)):
                if i != 0:
                    if unit_2.units[i].heal_power > 0:
                        unit_2.units[i].heal(unit_2.units[i - 1])

            if len(unit_2.units) == 0:
                return True


            if unit_2.units[0].attack > unit_1.units[0].defense:  # 判断 防御值 ----
                unit_1.units[0].health = unit_1.units[0].health - unit_2.units[0].attack + unit_1.units[0].defense  # 造成伤害
                unit_2.units[0].health = unit_2.units[0].health + (unit_2.units[0].attack - unit_1.units[0].defense) * unit_2.units[
                    0].vampirism*0.01  # 吸血
                if unit_2.units[0].health>unit_2.units[0].max_health:
                    unit_2.units[0].health=unit_2.units[0].max_health
            if len(unit_1.units) > 1:  # 判断穿透
                unit_1.units[1].health = unit_1.units[1].health - unit_2.units[0].attack * unit_2.units[0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_1.units)):
                if unit_1.units[i].health > 0:
                    temp.append(unit_1.units[i])
            unit_1.units = temp
            for i in range(0, len(unit_1.units)):
                if i != 0:
                    if unit_1.units[i].heal_power > 0:
                        unit_1.units[i].heal(unit_1.units[i - 1])
            if len(unit_1.units) == 0:
                return False

    def straight_fight(self, unit_1, unit_2):
        while 1:
            temp1 = []
            temp2 = []
            if len(unit_1.units) > len(unit_2.units):
                for i in range(0,len(unit_2.units)):
                    if fight(unit_1.units[i],unit_2.units[i]) :
                        temp1.append(unit_1.units[i])
                    else :
                        temp2.append(unit_2.units[i])
                for i in range(len(unit_2.units),len(unit_1.units)):
                    temp1.append(unit_1.units[i])


            if len(unit_2.units) > len(unit_1.units):
                for i in range(0,len(unit_1.units)):
                    if fight(unit_1.units[i],unit_2.units[i]) :
                        temp1.append(unit_1.units[i])
                    else :
                        temp2.append(unit_2.units[i])
                for i in range(len(unit_1.units),len(unit_2.units)):
                    temp1.append(unit_2.units[i])


            unit_1.units = temp1
            unit_2.units = temp2
            if len(unit_1.units) == 0:
                return False
            if len(unit_2.units) == 0:
                return True
class Weapon:
    def __init__(self,health,attack,defense ,vampirism  ,heal_power):
        self.health=health
        self.attack=attack
        self.defense=defense
        self.vampirism=vampirism
        self.heal_power=heal_power
class Sword:
    def __init__(self):
        self.health=5
        self.attack=2
        self.defense=0
        self.vampirism=0
        self.heal_power=0
class Shield:
    def __init__(self):
        self.health=20
        self.attack=-1
        self.defense=2
        self.vampirism=0
        self.heal_power=0
class GreatAxe:
    def __init__(self):
        self.health=-15
        self.attack=5
        self.defense=-2
        self.vampirism=10
        self.heal_power=0
class Katana:
    def __init__(self):
        self.health=-20
        self.attack=6
        self.defense=-5
        self.vampirism=50
        self.heal_power=0
class MagicWand:
    def __init__(self):
        self.health=30
        self.attack=3
        self.defense=0
        self.vampirism=0
        self.heal_power=3

ogre = Warrior()
lancelot = Knight()
richard = Defender()
eric = Vampire()
freelancer = Lancer()
priest = Healer()

sword = Sword()
shield = Shield()
axe = GreatAxe()
katana = Katana()
wand = MagicWand()
super_weapon = Weapon(50, 10, 5, 150, 8)

ogre.equip_weapon(sword)
ogre.equip_weapon(shield)
ogre.equip_weapon(super_weapon)
lancelot.equip_weapon(super_weapon)
richard.equip_weapon(shield)
eric.equip_weapon(super_weapon)
freelancer.equip_weapon(axe)
freelancer.equip_weapon(katana)
priest.equip_weapon(wand)
priest.equip_weapon(shield)

assert ogre.health == 125
assert lancelot.attack == 17
assert richard.defense == 4
assert eric.vampirism == 200
assert freelancer.health == 15
assert priest.heal_power == 5

assert fight(ogre, eric) == False
assert fight(priest, richard) == False
assert fight(lancelot, freelancer) == True

my_army = Army()
my_army.add_units(Knight, 1)
my_army.add_units(Lancer, 1)

enemy_army = Army()
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 1)

my_army.units[0].equip_weapon(axe)
my_army.units[1].equip_weapon(super_weapon)

enemy_army.units[0].equip_weapon(katana)
enemy_army.units[1].equip_weapon(wand)

battle = Battle()

assert battle.fight(my_army, enemy_army) == True