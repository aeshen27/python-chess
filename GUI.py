#GUI

#Abby Shen
#
#new ChessGUI

from graphics import *
from Square import Square
from modifiedButton import Button


class ChessGUI:
  """This class contains the Chess visual interface."""

  def __init__(self):
    self.win = GraphWin("Chess", 800, 600)
    self.win.setBackground("beige")
    self.squarelist = []
    y = 125
    saddlebrown = 0
    for i in range(8):
      x = 75
      letter = 97
      number = i + 1
      for i in range(8):
        if saddlebrown % 2 == 0:
          color = "saddlebrown"
        else:
          color = "tan"
        square = Square(Point(x, y), color, chr(letter) + str(number))
        self.squarelist.append(square)
        saddlebrown += 1
        letter += 1
        x += 50
      saddlebrown += 1
      y += 50
    for square in self.squarelist:
      rectangle = square.getSquare()
      rectangle.draw(self.win)
    self.messageboard = Rectangle(Point(500, 200), Point(750, 400))
    self.messageboard.setOutline("saddlebrown")
    self.messageboard.setFill("tan")
    self.messageboard.draw(self.win)
    self.message = Text(Point(625, 300), "Welcome.")
    self.message.draw(self.win)
    num = 97
    for i in range(8):
      abc = Text(Point((25 + 50 * (i + 1)), 85), chr(num))
      abc.draw(self.win)
      num += 1
    for i in range(8):
      numbers = Text(Point(465, (525 - (50 * (i + 1)))), str(i + 1))
      numbers.draw(self.win)
    self.quitbutton = Button(Point(725, 50), 50, 25, "Quit")
    buttonRectangle = self.quitbutton.getRectangle()
    buttonRectangle.setFill("tan")
    buttonRectangle.draw(self.win)
    buttonText = self.quitbutton.getText()
    buttonText.draw(self.win)

  def squareActivate(self, piecelist):
    for square in piecelist:
      x = square[0]
      y = square[1]
      index = int((x - 1) + (y - 1) * 8)
      activatedsquare = self.squarelist[index]
      activatedsquare.activate()

  def squareDeactivate(self, piecelist):
    for square in piecelist:
      x = square[0]
      y = square[1]
      index = int((x - 1) + (y - 1) * 8)
      deactivatedsquare = self.squarelist[index]
      deactivatedsquare.deactivate()

  def squareHighlight(self, possibleMoveList):
    for square in possibleMoveList:
      x = square[0]
      y = square[1]
      index = int((x - 1) + (y - 1) * 8)
      highlightedsquare = self.squarelist[index]
      highlightedsquare.highlight()
      highlightedsquare.activate()

  def locationsToSquareList(self, locationlist):
    newsquarelist = []
    for location in locationlist:
      x = location[0]
      y = location[1]
      index = int((x - 1) + (y - 1) * 8)
      square = self.squarelist[index]
      newsquarelist.append(square)
    return newsquarelist

  def printLabels(self, squarelist):
    for square in squarelist:
      print(square.getLabel())

  def unhighlightAll(self):
    for square in self.squarelist:
      square.unhighlight()

  def getClick(self):
    return self.win.getMouse()

  def checkQuitButton(self, pt):
    if self.quitbutton.clicked(pt):
      return True
    else:
      return False


#not sure if it was possible to add an optional parameter but this was my way of doing it

  def checkSquareClick(self, point, list):
    if list == "all":
      for square in self.squarelist:
        if square.clicked(point) == True:
          return True
      return False
    else:
      for square in list:
        if square.clicked(point) == True:
          return True
      return False

  def getClickedSquare(self, point, list):
    if list == "all":
      for square in self.squarelist:
        if square.clicked(point) == True:
          square.highlight()
          return square.getLabel()
    else:
      for square in list:
        if square.clicked(point) == True:
          square.highlight()
          return square.getLabel()

  def checkSquareActive(self):
    activesquares = []
    for square in self.squarelist:
      active = square.checkActive()
      activesquares.append(active)
    return activesquares

  def closeWindow(self):
    self.win.close()

  def unhighlight(self, unhighlightlist):
    for square in unhighlightlist:
      x = square[0]
      y = square[1]
      index = int((x - 1) + (y - 1) * 8)
      unhighlightedsquare = self.squarelist[index]
      unhighlightedsquare.unhighlight()

  #change these two so that it is just a "set text" function that will work for both
  def blackTurn(self):
    self.message.setText("It is black's move.")

  def whiteTurn(self):
    self.message.setText("It is white's move.")

  def move(self, piece, oldsquare, newsquare):
    self.pieceDraw(piece, newsquare)
    self.pieceUndraw(oldsquare)

  def eatMove(self, piece, oldsquare, newsquare):
    self.pieceUndraw(newsquare)
    self.pieceDraw(piece, newsquare)
    self.pieceUndraw(oldsquare)

  def pieceDraw(self, piece, square):
    x = square[0] * 50 + 25
    y = square[1] * 50 + 75
    pieceImage = Image(Point(x, y), piece + ".png")
    pieceImage.draw(self.win)

  def pieceUndraw(self, square):
    x = square[0]
    y = square[1]
    index = int((x - 1) + (y - 1) * 8)
    redrawnsquare = self.squarelist[index]
    rectangle = redrawnsquare.getSquare()
    newrectangle = rectangle.clone()
    newrectangle.draw(self.win)

  def setBoard(self):
    self.pieceDraw("whiteKing", [4, 8])
    self.pieceDraw("blackKing", [4, 1])
    self.pieceDraw("whiteQueen", [5, 8])
    self.pieceDraw("blackQueen", [5, 1])
    self.pieceDraw("whiteBishop", [3, 8])
    self.pieceDraw("whiteBishop", [6, 8])
    self.pieceDraw("blackBishop", [3, 1])
    self.pieceDraw("blackBishop", [6, 1])
    self.pieceDraw("whiteKnight", [2, 8])
    self.pieceDraw("whiteKnight", [7, 8])
    self.pieceDraw("blackKnight", [2, 1])
    self.pieceDraw("blackKnight", [7, 1])
    self.pieceDraw("blackRook", [1, 1])
    self.pieceDraw("blackRook", [8, 1])
    self.pieceDraw("whiteRook", [1, 8])
    self.pieceDraw("whiteRook", [8, 8])
    for i in range(8):
      self.pieceDraw("blackPawn", [(i + 1), 2])
    for i in range(8):
      self.pieceDraw("whitePawn", [(i + 1), 7])

  #genius code in my opinion but we don't need it anymore :(
  #index = (ord(square[0])-97)+int(square[1])*8
  #highlightedsquare = self.squarelist[index]
  #highlightedsquare.highlight()
  #highlightedsquare.activate()
   
                      
