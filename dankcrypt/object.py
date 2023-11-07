import uuid

class Object:
  def __init__(self, title, equippable = True, equippableSlots = []):
    self.title = title
    self.id = uuid.uuid4()
    self.equippable = equippable
    self.equipped = False
    self.equippableSlots = equippableSlots

  def getId(self):
    return self.id