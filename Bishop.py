#Bishop

class Bishop():

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
    return ("Bishop")
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
    self.potential = self.potentiallu + self.potentialld + self.potentialru + self.potentialrd
    return self.potential
