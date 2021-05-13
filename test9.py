

class Warrior:  #战士类
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.attack = 5
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0
        self.move = 0
        self.flag = "Warrior"

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):     #装备武器方法
        self.health = self.health + weapon.health
        self.max_health = self.max_health + weapon.health
        if self.attack != 0:    #没有的属性不加不减,有的才加减
            self.attack = self.attack + weapon.attack
            if self.attack < 0:
                self.attack = 0
        if self.defense != 0:
            self.defense = self.defense + weapon.defense
            if self.defense < 0:
                self.defense = 0
        if self.vampirism != 0:
            self.vampirism = self.vampirism + weapon.vampirism
            if self.vampirism < 0:
                self.vampirism = 0
        if self.heal_power != 0:
            self.heal_power = self.heal_power + weapon.heal_power
            if self.heal_power < 0:
                self.heal_power = 0

#各种士兵类
class Knight(Warrior):      #骑士类
    def __init__(self):
        self.max_health = 50
        self.attack = 7
        self.defense = 0
        self.health = 50
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0
        self.move = 0
        self.flag = "Warrior"


class Defender(Warrior):
    def __init__(self):
        self.max_health = 60
        self.attack = 3
        self.health = 60
        self.defense = 2
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0
        self.move = 0
        self.flag = "Warrior"


class Vampire(Warrior):
    def __init__(self):
        self.max_health = 40
        self.attack = 4
        self.health = 40
        self.defense = 0
        self.vampirism = 50
        self.through = 0
        self.heal_power = 0
        self.move = 0
        self.flag = "Warrior"


class Lancer(Warrior):
    def __init__(self):
        self.attack = 6
        self.max_health = 50
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.through = 0.5
        self.heal_power = 0
        self.move = 0
        self.flag = "Lancer"


class Healer(Warrior):
    def __init__(self):
        self.attack = 0
        self.health = 60
        self.max_health = 60
        self.defense = 0
        self.vampirism = 0
        self.through = 0
        self.heal_power = 2
        self.move = 0
        self.flag = "Healer"

    def heal(self, rapist):     #治疗方法
        rapist.health = rapist.health + self.heal_power
        if rapist.health > rapist.max_health:   #治疗不能超过最大血量
            rapist.health = rapist.max_health


class Warlord(Warrior):
    def __init__(self):
        self.attack = 4
        self.health = 100
        self.max_health = 100
        self.defense = 2
        self.vampirism = 0
        self.through = 0
        self.heal_power = 0
        self.move = 1       #move =1 区分战争贩子
        self.flag = "Warrior"   #标签


def fight(unit_1, unit_2):
    while 1:
        if unit_1.attack > unit_2.defense:  # 判断 防御值 ----
            unit_2.health = unit_2.health - unit_1.attack + unit_2.defense  # 造成伤害
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.defense) * unit_1.vampirism * 0.01  # 吸血
        if unit_2.health <= 0:
            return True
        if unit_2.attack > unit_1.defense:  # 判断 防御值 ----
            unit_1.health = unit_1.health - unit_2.attack + unit_1.defense  # 造成伤害
            unit_2.health = unit_2.health + (unit_2.attack - unit_1.defense) * unit_2.vampirism * 0.01  # 吸血
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, type, num):     #给军队加人，type是加的兵种，num是数量
        for i in range(0, num):
            obj = type()        #实例化
            self.units.append(obj)

    def move_units(self):       #warlord的方法
        temp_warlord = []
        for i in range(0, len(self.units)):
            if self.units[i].move == 0:     #将不是战争贩子的所有人放到新数组
                temp_warlord.append(self.units[i])
        if len(temp_warlord) == len(self.units):        #没有不能调用此方法
            return False
        else:   #有的话就让老数组等于新数组，在最后加一个战争贩子
            self.units = temp_warlord
            self.add_units(Warlord, 1)
        for i in range(0, len(self.units)):
            temp3 = []
            if self.units[i].move == 1:  # 判断有无战争贩子
                if i != len(self.units)-1:    #判断战争贩子在不在末尾
                    temp3.append(self.units[i])
                    del self.units[i]
                    self.units.insert(len(self.units), temp3[0])
                temp1 = []
                temp2 = []
                for j in range(0, len(self.units)):
                    if self.units[j].through > 0:  # 判断有无枪兵
                        temp1.append(self.units[j])
                        del self.units[j]
                        self.units.insert(0, temp1[0])
                    if self.units[j].heal_power != 0 : #判断有无治疗者
                        temp2.append(self.units[j])
                        del self.units[j]
                        self.units.insert(1, temp2[0])
                if self.units[0].heal_power != 0:      #避免初始数组的一二位都是治疗者
                    temp1 = []
                    for i in range(0, len(self.units)):
                        if self.units[i].heal_power != 0:
                            temp1.append(self.units[i])
                            del self.units[i]
                            self.units.insert(0, temp1[0])
                            break
        return True


class Battle:
    def fight(self, unit_1, unit_2):
        # assert isinstance(unit_1, Army)
        while 1:
            if unit_1.units[0].attack > unit_2.units[0].defense:  # 判断 防御值 ----
                unit_2.units[0].health = unit_2.units[0].health - unit_1.units[0].attack + unit_2.units[
                    0].defense  # 造成伤害
                unit_1.units[0].health = unit_1.units[0].health + (unit_1.units[0].attack - unit_2.units[0].defense) * \
                                         unit_1.units[
                                             0].vampirism * 0.01  # 吸血
                if unit_1.units[0].health > unit_1.units[0].max_health:
                    unit_1.units[0].health = unit_1.units[0].max_health     #防止血量超过最大血量
            if len(unit_2.units) > 1:  # 判断穿透
                unit_2.units[1].health = unit_2.units[1].health - unit_1.units[0].attack * unit_1.units[
                    0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_2.units)):
                if unit_2.units[i].health > 0:
                    temp.append(unit_2.units[i])
            if len(unit_2.units) != len(temp):  #判断是否死人
                unit_2.units = temp     #如果死了人就调用方法
                unit_2.move_units()
            for i in range(0, len(unit_2.units)):
                if i != 0:  #加血
                    if unit_2.units[i].heal_power > 0:
                        unit_2.units[i].heal(unit_2.units[i - 1])
            if len(unit_2.units) == 0:  #二队死完了，返回TRUE
                return True

            if unit_2.units[0].attack > unit_1.units[0].defense:  # 判断 防御值 ----剩下的同上
                unit_1.units[0].health = unit_1.units[0].health - unit_2.units[0].attack + unit_1.units[
                    0].defense  # 造成伤害
                unit_2.units[0].health = unit_2.units[0].health + (unit_2.units[0].attack - unit_1.units[0].defense) * \
                                         unit_2.units[
                                             0].vampirism * 0.01  # 吸血
                if unit_2.units[0].health > unit_2.units[0].max_health:
                    unit_2.units[0].health = unit_2.units[0].max_health
            if len(unit_1.units) > 1:  # 判断穿透
                unit_1.units[1].health = unit_1.units[1].health - unit_2.units[0].attack * unit_2.units[
                    0].through  # 造成伤害
            temp = []
            for i in range(0, len(unit_1.units)):
                if unit_1.units[i].health > 0:
                    temp.append(unit_1.units[i])
            unit_1.units = temp
            unit_1.move_units()
            for i in range(0, len(unit_1.units)):
                if i != 0:
                    if unit_1.units[i].heal_power > 0:
                        unit_1.units[i].heal(unit_1.units[i - 1])
            if len(unit_1.units) == 0:
                return False    #一队死完了，返回FALSE

    def straight_fight(self, unit_1, unit_2):           #单挑战术
        while 1:
            temp1 = []
            temp2 = []
            if len(unit_1.units) > len(unit_2.units):   #一队伍更长的时候
                for i in range(0, len(unit_2.units)):
                    if fight(unit_1.units[i], unit_2.units[i]):     #让双方第i-1个人单挑
                        temp1.append(unit_1.units[i])       #单挑结果是true的话执行这个
                    else:   #单挑结果是false的话执行这个
                        temp2.append(unit_2.units[i])
                for i in range(len(unit_2.units), len(unit_1.units)):   #把多余的几个人放到新数组
                    temp1.append(unit_1.units[i])

            if len(unit_2.units) > len(unit_1.units):       #同上，二队伍更长的时候
                for i in range(0, len(unit_1.units)):
                    if fight(unit_1.units[i], unit_2.units[i]):
                        temp1.append(unit_1.units[i])
                    else:
                        temp2.append(unit_2.units[i])
                for i in range(len(unit_1.units), len(unit_2.units)):
                    temp1.append(unit_2.units[i])
            unit_1.units = temp1    #让老数组等于新数组，开始下一轮打架
            unit_2.units = temp2
            if len(unit_1.units) == 0:      #打到第一组或者第二组都死完的时候结束，一组赢TRUE，二组赢FALSE
                return True
            if len(unit_2.units) == 0:
                return False


class Weapon:   #武器类
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword:
    def __init__(self):
        self.health = 5
        self.attack = 2
        self.defense = 0
        self.vampirism = 0
        self.heal_power = 0


class Shield:
    def __init__(self):
        self.health = 20
        self.attack = -1
        self.defense = 2
        self.vampirism = 0
        self.heal_power = 0


class GreatAxe:
    def __init__(self):
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10
        self.heal_power = 0


class Katana:
    def __init__(self):
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50
        self.heal_power = 0


class MagicWand:
    def __init__(self):
        self.health = 30
        self.attack = 3
        self.defense = 0
        self.vampirism = 0
        self.heal_power = 3


ronald = Warlord()
heimdall = Knight()

assert fight(heimdall, ronald) == False

my_army = Army()
my_army.add_units(Warlord, 1)
my_army.add_units(Warrior, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 2)

enemy_army = Army()
enemy_army.add_units(Warlord, 3)
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 2)
enemy_army.add_units(Knight, 2)

my_army.move_units()
enemy_army.move_units()

assert type(my_army.units[0]) == Lancer
assert type(my_army.units[1]) == Healer
assert type(my_army.units[-1]) == Warlord

assert type(enemy_army.units[0]) == Vampire
assert type(enemy_army.units[-1]) == Warlord
assert type(enemy_army.units[-2]) == Knight

# 6, not 8, because only 1 Warlord per army could be
assert len(enemy_army.units) == 6

battle = Battle()

assert battle.fight(my_army, enemy_army) == True
