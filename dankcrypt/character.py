from .object import *

class Character:
  def __init__(self, title):
    self.title = title
    self.id = uuid.uuid4()
    self.attack = 1
    self.defense = 1
    self.health = 1
    self.stamina = 1
    self.magic = 1
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
    self.slots = self.equipment.keys()
    
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
  
  #TODO: work on XP table and leveling curves 
  def levelUp(self):
    self.level

