'''
CLass to creating magic
'''

from .character import Character


class Spell(Character):
    def __init__(self, name, cost, dmg, typ):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.typ = typ

    def generate_dmg(self):
        return self.dmg


# Create Spells
fire = Spell("Fire", 25, 600, "dmg")
thunder = Spell("Thunder", 25, 600, "dmg")
blizzard = Spell("Blizzard", 25, 600, "dmg")
meteor = Spell("Meteor", 40, 1200, "dmg")
quake = Spell("Quake", 14, 140, "dmg")

cure = Spell("Cure", 25, 620, "heal")
cura = Spell("Cura", 32, 1500, "heal")
satan = Spell("Codex Gigas", 50, 6000, "heal")

# lists of spells
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, satan]
