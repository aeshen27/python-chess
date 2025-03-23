#Rook

class Rook():

  def __init__(self, x, y, color):
    self.alive = True
    self.active = True
    self.color = color
    #self.positions = []
    self.x = x
    self.y = y

  def getType(self):
    return ("Rook")

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
    self.potentialu = []
    self.potentiald = []
    self.potentiall = []
    self.potentialr = []
    clearu = True
    u = 1
    while clearu and (y + u) <= 8:
      for i in positions:
        if i[0] == x and i[1] == y + u:
          if positions[i] != self.color:
            self.potentialu.append((x, y + u))
          clearu = False
          break
      if clearu == True:
        self.potentialu.append((x, y + u))
        u += 1
    cleard = True
    d = 1
    while cleard and (y - d) >= 1:
      for i in positions:
        if i[0] == x and i[1] == y - d:
          if positions[i] != self.color:
            self.potentialu.append((x, y - d))
          cleard = False
          break
      if cleard == True:
        self.potentiald.append((x, y - d))
        d += 1
    clearl = True
    l = 1
    while clearl and (x - l) >= 1:
      for i in positions:
        if i[0] == x - l and i[1] == y:
          if positions[i] != self.color:
            self.potentialu.append((x - l, y))
          clearl = False
          break
      if clearl == True:
        self.potentiall.append((x - l, y))
        l += 1
    clearr = True
    r = 1
    while clearr and (x + r) <= 8:
      for i in positions:
        if i[0] == x + r and i[1] == y:
          if positions[i] != self.color:
            self.potentialu.append((x + r, y))
          clearr = False
          break
      if clearr == True:
        self.potentialr.append((x + r, y))
        r += 1
    self.potentials = self.potentialu + self.potentiald + self.potentialr + self.potentiall
    return self.potentials


def main():
  rook = Rook("white")


# print("HI")
#print(rook.potential(2,1,{(2,2):"black"}))
