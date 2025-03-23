#Knight

class Knight():

  def __init__(self, x, y, color):
    self.alive = True
    self.active = True
    self.color = color
    #self.positions = []
    self.x = x
    self.y = y

  def getType(self):
    return ("Knight")

  def getColor(self):
    return self.color

  def movement(self, newpos):
    self.y = newpos[1]
    self.x = newpos[0]

  def getLocationx(self):
    return self.x

  def getLocationY(self):
    return self.y

  def getLocation(self):
    return (self.x, self.y)

  def remove(self):
    self.alive = False

  def potential(self, x, y, positions):

    self.potentialru = []
    self.potentiallu = []
    self.potentialrd = []
    self.potentialld = []
    r = 1
    d = 2
    clearrd = True
    if (y - d) >= 1 and (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialrd.append((x + r, y - d))
          clearrd = False
          break
      if clearrd == True:
        self.potentialrd.append((x + r, y - d))

    r = 2
    d = 1
    clearrd = True
    if (y - d) >= 1 and (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialrd.append((x + r, y - d))
          clearrd = False
          break
      if clearrd == True:
        self.potentialrd.append((x + r, y - d))
    r = 2
    u = 1
    clearru = True
    if (y + u) <= 8 and (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialru.append((x + r, y + u))
          clearru = False
          break
      if clearru == True:
        self.potentialrd.append((x + r, y + u))

    r = 1
    u = 2
    clearru = True
    if (y + u) <= 8 and (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialru.append((x + r, y + u))
          clearru = False
          break
      if clearru == True:
        self.potentialrd.append((x + r, y + u))
    l = 1
    d = 2
    clearld = True
    if (y - d) >= 1 and (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialrd.append((x - l, y - d))
          clearld = False
          break
      if clearld == True:
        self.potentialrd.append((x - l, y - d))
    l = 2
    d = 1
    clearld = True
    if (y - d) >= 1 and (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialrd.append((x - l, y - d))
          clearld = False
          break
      if clearld == True:
        self.potentialrd.append((x - l, y - d))
    l = 2
    u = 1
    clearlu = True
    if (y + u) <= 8 and (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialru.append((x - l, y + u))
          clearlu = False
          break
      if clearlu == True:
        self.potentialrd.append((x - l, y + u))
    clearlu = True
    l = 1
    u = 2
    if (y + u) <= 8 and (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialru.append((x - l, y + u))
          clearlu = False
          break
      if clearlu == True:
        self.potentialrd.append((x - l, y + u))

    self.potentials = self.potentiallu + self.potentialld + self.potentialru + self.potentialrd
    return self.potentials


#def main():
# night = Knight(2,3,"black")
#print("HI")
# print(night.potential(7,8,{(8,1):"white"}))
