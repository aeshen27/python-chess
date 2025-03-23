#Queen

class Queen():

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
    return ("Queen")

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
    ru = 1
    while clearru and (y + ru) <= 8 and (x + ru) <= 8:
      for i in positions:
        if i[0] == x + ru and i[1] == y + ru:
          if positions[i] != self.color:
            self.potentialru.append((x + ru, y + ru))
          clearru = False
          break
      if clearru == True:
        self.potentialru.append((x + ru, y + ru))
        ru += 1
    clearrd = True
    rd = 1
    while clearrd and (y - rd) >= 1 and (x + rd) <= 8:
      for i in positions:
        if i[0] == x + rd and i[1] == y - rd:
          if positions[i] != self.color:
            self.potentialrd.append((x + rd, y - rd))
          clearrd = False
          break
      if clearrd == True:
        self.potentialrd.append((x + rd, y - rd))
        rd += 1
    clearld = True
    ld = 1
    while clearld and (x - ld) >= 1 and (y - ld) >= 1:
      for i in positions:
        if i[0] == x - ld and i[1] == y - ld:
          if positions[i] != self.color:
            self.potentialld.append((x - ld, y - ld))
          clearld = False
          break
      if clearld == True:
        self.potentialld.append((x - ld, y - ld))
        ld += 1
    clearlu = True
    lu = 1
    while clearlu and (x - lu) >= 1 and (y + lu) <= 8:
      for i in positions:
        if i[0] == x - lu and i[1] == y + lu:
          if positions[i] != self.color:
            self.potentiallu.append((x - lu, y + lu))
          clearlu = False
          break
      if clearlu == True:
        self.potentiallu.append((x - lu, y + lu))
        lu += 1

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
    self.potentials = self.potentiallu + self.potentialld + self.potentialru + self.potentialrd + self.potentialu + self.potentiald + self.potentialr + self.potentiall
    return self.potentials


def main():
  queen = Queen(1, 2, "white")
  #print("HI")
  print(queen.potential(5, 5, {(2, 2): "black"}))
