from dankcrypt import *


class HealthPotion(Object):

  def __init__(self, *args, **kwargs):
    super(HealthPotion, self).__init__(*args, **kwargs)
    self.consumable = True
    self.replenish = 5

  def consumeMethodStatAdjustment(self, character):
    if character.currentHealth + self.replenish < character.attributes['health']:
      character.currentHealth += self.replenish
      print("User " + character.title + " consumed " + self.title)
      print("Health went up by " + str(self.replenish) +  " to " + str(character.currentHealth))
    else:
      character.currentHealth = character.attributes['health']
      print("User " + character.title + " consumed " + self.title)
      print("Health went back to max.")


class ManaPotion(Object):

  def __init__(self, *args, **kwargs):
    super(ManaPotion, self).__init__(*args, **kwargs)
    self.consumable = True
    self.replenish = 5

  def consumeMethodStatAdjustment(self, character):
    if character.currentMana + self.replenish < character.attributes['mana']:
      character.currentMana += self.replenish
      print("User " + character.title + " consumed " + self.title)
      print("Mana went up by " + str(self.replenish) +  " to " + str(character.currentMana))
    else:
      character.currentMana = character.attributes['mana']
      print("User " + character.title + " consumed " + self.title)
      print("Mana went back to max.")
