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
        actions = ["east", "north", "west", "south"]
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
    nextPosition = self.getNextPosition(action, self.position)
    if(nextPosition == False):
      return "Invalid movement"
    else:
      self.position = nextPosition
      return "Now you are in the " + self.getPositionName(nextPosition)

  def getNextPosition(self, action, position = 0):
    if position == 0:
      position = self.position

    if action not in self.getLegalActions(position):
      return False

    actions = ["east", "north", "west", "south"]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y, = position
    index = actions.index(action)
    return (x+dx[index], y+dy[index])



  def getLegalActions(self, position = 0):
    if position == 0:
      position = self.position
    return self.legalActions[position]

  def getPosition(self, position = 0):
    if position == 0: position = self.position
    return self.house[position[0]][position[1]]

  def getPositionName(self, position = 0):
    if position == 0: position = self.position
    positionNames = ["Ilegal", "Bedroom", "Bathroom", "Kitchen", "Livingroom", "Office", "Hallway", "Porch"]
    return positionNames[self.getPosition(position)]

  def getMovementOptionsText(self):
    legalActions = self.getLegalActions()
    text = ["Go to the " + action + " to go to the " + self.getPositionName(self.getNextPosition(action)) for action in legalActions]
    return '\n'.join(text)


