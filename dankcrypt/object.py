import uuid


class Object:

  def __init__(self,
               title,
               equippable=False,
               consumable=False,
               equippableSlots=[]):
    self.title = title
    self.id = uuid.uuid4()
    self.equippable = equippable
    self.consumable = consumable
    self.equippableSlots = equippableSlots
    self.equipped = False

  def getId(self):
    return self.id

  # Performs stat adjustments to character that consumes this object
  def consumeMethodStatAdjustment(self, character):
    print("User " + character.title + " consumed " + self.title)
    print("No stat adjustments made, as this is the super method.")

  # Performs stat adjustments to character that equips this object
  def equipMethodStatAdjustment(self, character):
    print("User " + character.title + " equipped " + self.title)
    print("No stat adjustments made, as this is the super method.")
