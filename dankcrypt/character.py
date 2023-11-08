import random
from .object import *
from .engine import *

#TODO: find alternatives to counter
from collections import Counter


class Character:

  def __init__(self, title):
    self.title = title
    self.id = uuid.uuid4()
    self.gold = 0
    self.sprite = None
    self.posX = 0
    self.posY = 0
    self.width = 1
    self.height = 1

    # These are the skills you can put attribute points into
    self.attributes = {
        'attack': 1,  # probability to rolling a hit
        'strength': 1,  # how strong your hits will be
        'defense': 1,  # probability of blocking a hit
        'health': 10,  # health
        'stamina': 1,  # stamina, how long you can run
        'magic': 1,  # how strong your magical attacks can be
        'wisdom': 1,  # item/lore discovery rate
        'mana': 10  # how much spells you can cast
    }

    self.baseWeight = 5  # how big of a bbm you have at baseline
    self.maxLoad = (self.baseWeight / 4) + (self.attributes['strength'] / 4)
    self.exp = 0
    self.level = 0
    self.inventory = []

    self.equipment = {
        'head': None,
        'torso': None,
        'legs': None,
        'leftarm': None,
        'rightarm': None,
        'neck': None,
        'talisman1': None,
        'talisman2': None,
        'talisman3': None,
        'talisman4': None
    }

    self.statuses = {
        'poisoned': 0,
        'burned': 0,
        'drenched': 0,
        'confused': 0,
        'paralyzed': 0,
        'bloodless': 0
    }  # Status effects are a percentage of buildup

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
      print('Added ' + object.title + ' with id ' + str(object.id) +
            ' to inventory.')

  def removeFromInventory(self, object):
    # allows you to pass in an id or an object
    id = object.id if isinstance(object, Object) else object
    for thing in self.inventory:
      if thing.id == id:
        self.inventory.remove(thing)
        print('Removed ' + thing.title + ' with id ' + str(thing.id) +
              ' from inventory.')
        return True
    return False

  def inInventory(self, object):
    return object.id in [thing.id for thing in self.inventory]

  def equipItem(self, object, slot):
    if object.equippable:
      if slot in object.equippableSlots:
        self.equipment[slot] = object
        # use the object's equip method
        object.equipMethodStatAdjustment(self)
        # mark this object as equipped now
        self.equipped = True
        return True  # successful equip
    else:
      print('Cannot equip ' + object.title + ' as object is not equippable.')
      return False  # unsuccessful equip

  def unequip(self, slot):
    if slot in self.equipment.keys():
      if isinstance(self.equipment[slot], Object):
        print('User ' + self.title + ' unequipped ' +
              self.equipment[slot].title + " from " + slot)
        # actually unequip item now
        self.equipment[slot].equipped = False
        self.equipment[slot] = None
      else:
        print('There is nothing to unequip in slot ' + slot)
      return True  # successful unequip
    else:
      print('Please provide a valid slot to unequip')
      return False  # unsuccessful unequip

  def consumeItem(self, object):
    # check to see if item is inventory, since only items in inventory can be consumed
    if self.inInventory(object):
      if object.consumable:
        # use the object's consume method
        object.consumeMethodStatAdjustment(self)
        # now that the object is consumed, remove it from the inventory.
        self.removeFromInventory(object.id)
        return True  # successful consume
      else:
        print('Cannot consume ' + object.title +
              ' as object is not consumable.')
        return False  # unsuccesful consume
    else:
      print("Attempted to consume item that wasn't in inventory")
      return False

  def giveExp(self, num=0):
    self.exp += num

  #TODO: work on XP table and leveling curves and point allotment
  def getExtraLevels(self):
    # the curves
    level = lambda exp: exp**(1 / 3)
    extraLevels = int(level(self.exp)) - self.level
    return extraLevels

  def getExtraExp(self):
    # the curves
    exp = lambda level: level**3  # exp(level) = level ** 3
    extraExp = self.exp - exp(self.level)
    return extraExp

  def levelUp(self, extraLevels, allotment=None):

    if allotment is None:
      allotment = {
          'attack': 0,
          'strength': 0,
          'defense': 0,
          'health': 0,
          'stamina': 0,
          'magic': 0,
          'wisdom': 0,
          'mana': 0
      }

    if extraLevels == sum(allotment.values()):
      # add stats to the character
      self.attributes = addDicts(self.attributes, allotment)
      # set a new level for the character
      self.level += extraLevels

  def applyDamage(self, value):
    if (self.health - value) > 0:
      self.health = self.health - value
    else:
      self.health = 0
      print('User ' + self.title + ' with id ' + str(self.id) + ' just died.')

  def applyStatusInflictions(self, statuses):
    self.statuses = addDicts(self.statuses, statuses)
    self.statuses = {
        key: value if value <= 1 else 1
        for key, value in self.statuses
    }

  def meleeAttack(self, slot, enemy):
    # get the weapon used for the attack
    if (self.equipment[slot]):
      # get the weapon that will be used for attacking
      weapon = self.equipment[slot]

      # get the adjusted attributes of the character attacking and the victim
      modifiedAttackerAttributes = dict(
          sum([Counter(self.attributes)] + [
              Counter(item.attributeBoost)
              for item in self.equipment if not None
          ]))
      modifiedVictimAttributes = dict(
          sum([Counter(enemy.attributes)] + [
              Counter(item.attributeBoost)
              for item in enemy.equipment if not None
          ]))
      modifiedAttackerStatusInflictions = dict(
          sum([
              Counter(item.statusInflictions) for item in self.equipment
              if not None
          ]))
      modifiedVictimStatusResistances = dict(
          sum([
              Counter(item.statusResistances) for item in enemy.equipment
              if not None
          ]))
      # make sure none of the percentage values in modifiedVictimStatusResistances are greater than 1
      modifiedVictimStatusResistancesClean = {
          key: value if value <= 1 else 1
          for key, value in modifiedVictimStatusResistances.items()
      }

      # roll to see if the attack lands
      cutoff = (50 + ((modifiedAttackerAttributes['attack'] -
                       modifiedVictimAttributes['defense']) / 100) * 50) / 100
      if random.random() <= cutoff:
        # attack landed, TODO: make a more complex formula involving strength
        enemy.applyDamage(self.modifiedAttackerAttributes['strength'])
        # inflict status effect minus any status infliction resistances
        negatedStatusInfliction = multiplyDicts(modifiedVictimStatusResistancesClean, modifiedAttackerStatusInflictions)
        
        enemy.applyStatusInflictions(
            subtractDicts(modifiedAttackerStatusInflictions, negatedStatusInfliction))
      else:
        # attack missed
        print('User ' + self.title + ' missed a melee attack on ' +
              enemy.title)
    else:
      # bare hands
      pass
