#Pawn

class Pawn():

  def __init__(self, x, y, color):
    self.alive = True
    self.active = True
    self.x = x
    self.color = color
    self.y = y

  def getColor(self):
    return self.color

  def getType(self):
    return ("Pawn")

  def movement(self, newpos):
    self.y = newpos[1]
    self.x = newpos[0]

  def getLocationx(self):
    return self.x

  def getLocationY(self):
    return self.y

  def getLocation(self):
    return (self.x, self.y)

  def remove():
    self.alive = False

  def potential(self, x, y, positions):
    self.potentials = []
    u = 1
    clearu = True
    clear2u = True
    clearru = False
    clearlu = False
    if self.color == "white":
      for i in positions:
        if i[0] == x and i[1] == y + 1:
          clearu = False
        if (i[0] == x and i[1] == y + 2) or y != 2:
          clear2u = False
        if i[0] == x + 1 and i[1] == y + 1 and positions[i] != self.color:
          clearru = True
        if i[0] == x - 1 and i[1] == y + 1 and positions[i] != self.color:
          clearlu = True

      if clearu == True:
        self.potentials.append((x, y + 1))
      if clear2u == True:
        self.potentials.append((x, y + 2))
      if clearlu == True:
        self.potentials.append((x - 1, y + 1))
      if clearru == True:
        self.potentials.append((x + 1, y + 1))
      return self.potentials
    if self.color == "black":
      for i in positions:
        if i[0] == x and i[1] == y - 1:
          clearu = False
        if (i[0] == x and i[1] == y - 2) or y != 7:
          clear2u = False
        if i[0] == x + 1 and i[1] == y - 1 and positions[i] != self.color:
          clearru = True
        if i[0] == x - 1 and i[1] == y - 1 and positions[i] != self.color:
          clearlu = True

      if clearu == True:
        self.potentials.append((x, y - 1))
      if clear2u == True:
        self.potentials.append((x, y - 2))
      if clearlu == True:
        self.potentials.append((x - 1, y - 1))
      if clearru == True:
        self.potentials.append((x + 1, y - 1))
      return self.potentials
