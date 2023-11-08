from dankcrypt import *


class HealthPotion(Object):

  def __init__(self, *args, **kwargs):
    super(HealthPotion, self).__init__(*args, **kwargs)
    self.consumable = True

  def consumeMethodStatAdjustment(self, character):
    super().consumeMethodStatAdjustment(character)


class ManaPotion(Object):

  def __init__(self, *args, **kwargs):
    super(HealthPotion, self).__init__(*args, **kwargs)
    self.consumable = True

  def consumeMethodStatAdjustment(self, character):
    super().consumeMethodStatAdjustment(character)
