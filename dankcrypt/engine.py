# helper functions
import dankcrypt
import json


def multiplyDicts(dict1, dict2):
  return {k: v * dict2[k] for k, v in dict1.items() if k in dict2}


def addDicts(dict1, dict2):
  return {k: v + dict2[k] for k, v in dict1.items() if k in dict2}


def subtractDicts(dict1, dict2):
  return {k: v - dict2[k] for k, v in dict1.items() if k in dict2}


class Engine:

  def __init__(self, title):
    self.title = title
    self.mapData = None
    self.playerChar = None

    # contains the objects that are adjacent to the player character's current position.
    self.adjacentEntities = {
      'north': None,
      'south': None,
      'east': None,
      'west': None
    }

  # based on player's position, load in the entities nearby that 
  def loadAdjacentEntities(self):
    adjacentEntities = {}
    adjacentsPositions = self.playerChar.getAdjacentCells()
    for key, value in adjacentsPositions.items():
      positionstring = str(value[0]) + ',' + str(value[1])
      adjacentEntities[key] = self.mapData[positionstring]

  
  def newGame(self, playerName, playerVocation):
    self.playerChar = dankcrypt.Character(playerName, playerVocation)
    self.initMapData('./assets/mapdata.json')
  
  # should load up a player character and a player map data
  def loadGame(self):
    pass


  def initMapData(self, path):
    # this function will load up the map JSON from memory. It will contain 9000^2 entries detailing the contents of the map.
    # 
    #
    #
    #
    #
    with open(path) as f:
        self.mapData = json.load(f)
  
