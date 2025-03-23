#Abby Shen
#
#this module contains our Square class

from graphics import *


class Square:
  """Square class. Acts as a modified button for Chess."""

  def __init__(self, center, color, label):
    #define parameters as instance variables
    self.center = center
    self.label = label
    self.color = color
    #find x and y components of the center coordinate
    self.centerX = self.center.getX()
    self.centerY = self.center.getY()
    #find the x and y components of the opposite corners of the button
    self.x1 = self.centerX - 25
    self.y1 = self.centerY + 25
    self.x2 = self.centerX + 25
    self.y2 = self.centerY - 25
    #make those components into points
    point1 = Point(self.x1, self.y1)
    point2 = Point(self.x2, self.y2)
    #create rectangle with those two points and draw it
    self.square = Rectangle(point1, point2)
    self.square.setFill(self.color)
    self.square.setOutline("saddlebrown")
    self.active = False

  def getSquare(self):
    return self.square

  def getLabel(self):
    return self.label

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

  def checkActive(self):
    return self.active

  def highlight(self):
    self.square.setFill("yellowgreen")

  def unhighlight(self):
    self.square.setFill(self.color)

  def clicked(self, point):
    return (self.active and self.x1 <= point.getX() <= self.x2
            and self.y2 <= point.getY() <= self.y1)
