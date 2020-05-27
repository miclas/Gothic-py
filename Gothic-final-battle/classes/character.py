from random import randrange
from .bcolors import bcolors
'''
Main class for character creation and the methods they (characters) need to fight
'''

class Character:
    def __init__(self, name, hp, mp, dmg, df, magic, items):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.dmg = dmg
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print('\n' + bcolors.MBOLD + self.name.replace(' ', '') + ':' + bcolors.ENDC)
        for action in self.actions:
            print(' ' + str(i) + ': ' + action)
            i += 1

    def generate_dmg(self):
        return randrange(self.dmg - round(.15 * self.dmg), self.dmg + round(0.15 * self.dmg))

    def take_dmg(self, dmg):
        atck = dmg - self.df
        if atck < 0:
            atck = 0
        self.hp -= atck
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def choose_magic(self):
        i = 1
        print('\n' + bcolors.MBLUE + bcolors.MBOLD + '    Grimoire:' + bcolors.ENDC)
        for spell in self.magic:
            print('     ' + str(i) + '.' + spell.name + '(cost:' + str(spell.cost) + ')')
            i += 1
        choice = int(input('     Choose spell: ')) - 1
        return choice

    def choose_item(self):
        i = 1
        print('\n' + bcolors.MBOLD + bcolors.MGREEN2 + '    Backpack:' + bcolors.ENDC)
        for item in self.items:
            print('     ' + str(i) + '.' + item['item'].name + ': ' + item['item'].description +
                  ' (x' + str(item['quantity']) + ')')
            i += 1
        choice = int(input('     Choose item: ')) - 1
        return choice

    def choose_target(self, enemies):
        i = 1
        print('\n' + bcolors.MYELLOW + bcolors.MBOLD + '     Target:' + bcolors.ENDC)
        for enemy in enemies:
            print('      ' + str(i) + '.', enemy.name)
            i += 1
        choice = int(input('      Choose target: ')) - 1
        return choice

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 25

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp = mp_string

        print("                         _________________________              __________ ")
        print(bcolors.MBOLD + self.name + "    " +
              current_hp + " |" + bcolors.MGREEN + hp_bar + bcolors.ENDC + "|    " +
              current_mp + " |" + bcolors.MBLUE + mp_bar + bcolors.ENDC + "|")

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                      __________________________________________________ ")
        print(bcolors.MBOLD + self.name + "  " +
              current_hp + " |" + bcolors.MRED + hp_bar + bcolors.ENDC + "|")


