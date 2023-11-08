from dankcrypt import *


class FireGreatSword(Object):

  def __init__(self, *args, **kwargs):
    super(FireGreatSword, self).__init__(*args, **kwargs)
    self.equippable = True
    self.equippableSlots = ['leftarm', 'rightarm']
    self.attributeBoost = {
        'attack': 5,  # probability to rolling a hit
        'strength': 0,  # how strong your hits will be
        'defense': 0,  # probability of blocking a hit
        'health': 0,  # health
        'stamina': 0,  # stamina, how long you can run
        'magic': 0,  # how strong your magical attacks can be
        'wisdom': 0,  # item/lore discovery rate
        'mana': 0  # how much spells you can cast
    }
    self.statusInflictions = {
        'poisoned': 0,
        'burned': 0.15,  # invokes a burn status effect
        'drenched': 0,
        'confused': 0,
        'paralyzed': 0,
        'bloodless': 0
    }
    # The percentage of status inflictions this item will let you resist
    self.statusResistances = {
        'poisoned': 0,
        'burned': 0,  
        'drenched': 0,
        'confused': 0,
        'paralyzed': 0,
        'bloodless': 0
    }

  # only stat adjustment that will be made is nothing
  def equipMethodStatAdjustment(self, character):
    print("User " + character.title + " equipped " + self.title)
    print("No stat adjustments made, as this weapon does not permanently change base stats.")
