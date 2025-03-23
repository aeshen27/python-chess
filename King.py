#King

class King():

  def __init__(self, x, y, color):
    self.alive = True
    self.active = True
    self.color = color
    #self.positions = []
    self.x = x
    self.y = y

  def getColor(self):
    return self.color

  def getType(self):
    return ("King")

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
    self.potentialu = []
    self.potentiald = []
    self.potentiall = []
    self.potentialr = []
    self.potentialru = []
    self.potentiallu = []
    self.potentialrd = []
    self.potentialld = []

    clearru = True
    if (y + 1) <= 8 and (x + 1) <= 8 and (y + 1) >= 1:
      for i in positions:
        if i[0] == x + 1 and i[1] == y + 1:
          if positions[i] != self.color:
            self.potentialru.append((x + 1, y + 1))
          clearru = False
          break
      if clearru == True:
        self.potentialru.append((x + 1, y + 1))

    clearlu = True
    if (y + 1) <= 8 and (x - 1) >= 1 and (y + 1) >= 1:
      for i in positions:
        if i[0] == x - 1 and i[1] == y + 1:
          if positions[i] != self.color:
            self.potentiallu.append((x - 1, y + 1))
          clearlu = False
          break
      if clearlu == True:
        self.potentiallu.append((x - 1, y + 1))

    clearrd = True
    if (y - 1) >= 1 and (x + 1) <= 8:
      for i in positions:
        if i[0] == x + 1 and i[1] == y + 1:
          if positions[i] != self.color:
            self.potentialrd.append((x + 1, y - 1))
          clearrd = False
          break
      if clearrd == True:
        self.potentialrd.append((x + 1, y - 1))
    clearld = True
    if (y - 1) >= 1 and (x - 1) >= 1:
      for i in positions:
        if i[0] == x - 1 and i[1] == y - 1:
          if positions[i] != self.color:
            self.potentialld.append((x - 1, y - 1))
          clearld = False
          break
      if clearld == True:
        self.potentialrd.append((x - 1, y - 1))
    clearu = True
    u = 1
    if (y + u) <= 8:
      for i in positions:
        if i[0] == x and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialu.append((x, y + u))
          clearu = False
          break
      if clearu == True:
        self.potentialu.append((x, y + u))

    cleard = True
    d = 1
    if (y - d) >= 1:
      for i in positions:
        if i[0] == x and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialu.append((x, y - d))
          cleard = False
          break
      if cleard == True:
        self.potentiald.append((x, y - d))

    clearl = True
    l = 1
    if (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y:
          if positions[i] != self.color:
            self.potentialu.append((x - l, y))
          clearl = False
          break
      if clearl == True:
        self.potentiall.append((x - l, y))

    clearr = True
    r = 1
    if (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y:
          if positions[i] != self.color:
            self.potentialu.append((x + r, y))
          clearr = False
          break
      if clearr == True:
        self.potentialr.append((x + r, y))

    self.potentials = self.potentialu + self.potentiald + self.potentialr + self.potentiall + self.potentiallu + self.potentialld + self.potentialru + self.potentialrd
    return self.potentials


def main():
  king = King(2, 3, "white")
  print("HI")
  print(king.potential(5, 5, {(6, 5): "white"}))
