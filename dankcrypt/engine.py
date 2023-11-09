# helper functions
def multiplyDicts(dict1, dict2):
  return {k: v * dict2[k] for k, v in dict1.items() if k in dict2}


def addDicts(dict1, dict2):
  return {k: v + dict2[k] for k, v in dict1.items() if k in dict2}


def subtractDicts(dict1, dict2):
  return {k: v - dict2[k] for k, v in dict1.items() if k in dict2}


class Engine:

  def __init__(self, title):
    self.title = title

  def initMapData(self):
    # this function will load up the map JSON from memory. It will contain 9000^2 entries detailing the contents of the map.
    # 
    #
    #
    #
    #
    pass