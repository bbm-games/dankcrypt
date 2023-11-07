from .object import *

class Character:
  def __init__(self, title):
    self.title = title
    self.id = uuid.uuid4()
    self.attack = 1          # probability to rolling a hit
    self.defense = 1         # probability of blocking a hit
    self.health = 10         # health
    self.stamina = 1         # stamina, how long you can run
    self.magic = 1           # how strong your magical attacks can be
    self.wisdom = 1          # item/lore discovery rate
    self.mana = 10           # how much spells you can cast
    self.baseWeight = 5      # how big of a bbm you have at baseline 
    self.strength = 1        # how strong your hits will be
    self.maxLoad = (self.baseWeight / 4) + (self.strength/4)
    self.exp = 0
    self.level = 0
    self.inventory = []
    self.equipment = {'head': None, 
                      'torso': None, 
                      'legs': None, 
                      'leftarm': None, 
                      'rightarm': None, 
                      'neck': None,
                      'talisman1': None,
                      'talisman2': None,
                      'talisman3': None,
                      'talisman4': None}
    self.statuses = {'poisoned': False,
                     'burned': False,
                     'drenched': False,
                     'confused': False,
                     'paralyzed': False,
                     'bloodless': False}
    self.statusEffects = self.statuses.keys()
    self.slots = self.equipment.keys()
    print('User ' + self.title + ' initiated with id ' + str(self.id))
    
  def getItemFromInventory(self, id):
    for item in self.inventory:
      if item.id == id:
        return item
    return None

  def addToInventory(self, object):
    if isinstance(object, Object):
      self.inventory.append(object)
      print('Added '+ object.title + ' with id ' + str(object.id) + ' to inventory.')

  def removeFromInventory(self, id):
    def thingy(thing):
      print('Removed '+ thing.title + ' with id ' + str(thing.id) + ' from inventory.')
      return thing
    self.inventory = [thingy(thing) for thing in self.inventory if thing.id != id]
    
  def equipItem(self, object, slot):
    if object.equippable:
      if slot in object.equippableSlots:
        self.equipment[slot] = object
      object.equipped = True
      print('Equipped ' + object.title + ' with id ' + str(object.id) + ' to slot ' + slot)
    else:
      return None
    
  def giveExp(self, num = 0):
    self.exp += num
  
  #TODO: work on XP table and leveling curves and point allotment 
  def levelUp(self):
    self.level

