import random

class Game:

  def __init__(self):
    self.position = (7,7)
    self.house = [[0 for x in range(15)] for y in range(15)]
    self.house[7][7] = 1
    self.legalActions = {}
    self.generateHouse()

  def generateHouse(self):
    possible = []
    def addPossible(pos, possible):
      for i in range(4):
        possible.append((pos,i))

    def addLegalAction(k, possible):
      while(True):
        actions = ["right", "up", "left", "down"]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        index = random.randint(0, len(possible)-1)

        pos, i = possible.pop(index)

        x, y = pos
        x2 = x+dx[i]
        y2 = y+dy[i]

        if(self.house[x2][y2] != 0):
          continue

        action = actions[i]
        self.house[x2][y2] = k
        if pos not in self.legalActions: self.legalActions[pos] = []
        self.legalActions[pos].append(actions[i])
        if (x2, y2) not in self.legalActions: self.legalActions[(x2, y2)] = []
        self.legalActions[(x2,y2)].append(actions[i-2])
        return((x2,y2))

    addPossible((7,7), possible)

    for k in range(2, 8):
      pos = addLegalAction(k, possible)
      addPossible(pos, possible)

  def printHouse(self):
    for i in range(13,-1,-1):
      for j in range(14):
        print self.house[j][i],
        print ' ',
      print '\n',

  def changePosition(self, action):
    if action not in self.getLegalActions(self.position):
      print("Ilegal Action")
      return False
    actions = ["right", "up", "left", "down"]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    if action in actions:
      x, y = self.position
      index = actions.index(action)
      self.position  = (x+dx[index], y+dy[index])

  def getLegalActions(self, position = 0):
    if position == 0:
      position = self.position
    return self.legalActions[position]

  def getPosition(self):
    print self.house[self.position[0]][self.position[1]]
