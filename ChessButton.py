#Abby Shen
#
#this module contains a button class modified for the Chess lab

from graphics import *

#win = GraphWin("test window", 600, 600)
#win.setBackground("white")

class Button:
    """Button class. Creates an invisible clickable button. All usual methods"""
    def __init__(self, center, width, height):
        #define parameters as instance variables
        self.center = center
        self.width = float(width)
        self.height = float(height)
        #find x and y components of the center coordinate
        self.centerX = self.center.getX()
        self.centerY = self.center.getY()
        #find the x and y components of the opposite corners of the button
        self.x1 = self.centerX - (self.width/2)
        self.y1 = self.centerY + (self.height/2)
        self.x2 = self.centerX + (self.width/2)
        self.y2 = self.centerY - (self.height/2)
        #make points with those x and y components
        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x2, self.y2)
        #create rectangle with those two points and draw it
        self.button = Rectangle(point1, point2)
        #self.button.draw(self.win)
        #self.text.draw(win)
        #start with the button inactive (not clickable)
        self.active = False
        
    def activate(self):
        self.active = True
    #deactivate by setting active to false and decreasing line weight
    def deactivate(self):
        self.active = False

    #return true if the button is active and the point given is within the bounds
    #of the button rectangle
    def clicked(self, point):
        return (self.active and
                self.x1 <= point.getX() <= self.x2 and
                self.y2 <= point.getY() <= self.y1)
    #fill the color of the rectangle
    def setFill(self, color):
        self.button.setFill(color)
    #set the color of the button outline
    def setOutline(self, color):
        self.button.setOutline(color)
        
    
#button = Button(win, Point(100, 100), 50, 20, "button")
#button.activate()
#button.clicked(win.getMouse())

