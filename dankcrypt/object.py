import uuid

class Object:
  def __init__(self, title):
    self.title = title
    self.id = uuid.uuid4()
    self.equippable = True
    self.equipped = False
    self.equippableSlots = []

  def getId(self):
    return self.id