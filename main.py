#main

from GUI import ChessGUI
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Queen import Queen
from King import King

from graphics import *


#"a1 -->1,1"
def convertor1(og):
  xconvert = ord(og[0]) - 96
  string = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
  yconvert = string[int(og[1])]
  return (xconvert, yconvert)


#1,1 --> 1,8
def convertor2(og):
  string = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
  yconvert = string[int(og[1])]
  return (og[0], yconvert)


#a1 --> 1,1
def convertor3(og):
  xconvert = ord(og[0]) + 48
  return (xconvert, og[1])


def makepositions(pieces):
  positions = {}
  for i in pieces:
    posx = i.getLocationx()
    posy = i.getLocationY()
    color = i.getColor()
    positions[(posx, posy)] = color
  return positions


def whiteTurn(gui, whitepiecelocations, whitepieces, positions):
  gui.whiteTurn()
  newwhitepiecelist = []
  for i in whitepiecelocations:
    newwhitepiecelist.append(convertor2(i))
  gui.squareActivate(newwhitepiecelist)
  moveMade = False
  while moveMade == False:
    while True:
      click = gui.getClick()
      if gui.checkQuitButton(click) == True:
        gui.closeWindow()
        break
      elif gui.checkSquareClick(click, "all") == True:
        gui.unhighlightAll()
       # gui.squareActivate(newwhitepiecelist)
        clickedsquare = gui.getClickedSquare(click, "all")
        break
    for i in whitepieces:
      if i.getLocation() == convertor1(clickedsquare):
        piece = i
    location = convertor1(clickedsquare)
    potential = piece.potential(location[0], location[1], positions)
    print(potential)
    newpotential = []
    for i in potential:
      newpotential.append(convertor2(i))
    gui.squareActivate(newpotential)
    gui.squareHighlight(newpotential)
    click2 = gui.getClick()
    potentialsquares = gui.locationsToSquareList(newpotential)
    if gui.checkSquareClick(click2, potentialsquares) == True:
      squaremoved = gui.getClickedSquare(click2, potentialsquares)
      gui.unhighlightAll()
      piecetype = piece.getType()
      piececolor = piece.getColor()
      movepiece = piececolor + piecetype
      piece.movement(convertor1(squaremoved))
      for i in positions:
        if convertor1(squaremoved) == i and positions[i] == "black":
          gui.eatMove(movepiece, convertor2(location), convertor2(convertor1(squaremoved)))
          moveMade = True
        else:
          gui.move(movepiece, convertor2(location),convertor2(convertor1(squaremoved)))
          moveMade = True


def blackTurn(gui, blackpiecelocations, blackpieces, positions):
  gui.blackTurn()
  newblackpiecelist = []
  for i in blackpiecelocations:
    newblackpiecelist.append(convertor2(i))
  gui.squareActivate(newblackpiecelist)
  moveMade = False
  while moveMade == False:
    while True:
      click = gui.getClick()
      if gui.checkQuitButton(click) == True:
        gui.closeWindow()
        break
      elif gui.checkSquareClick(click, "all") == True:
        gui.unhighlightAll()
        gui.squareActivate(newblackpiecelist)
        clickedsquare = gui.getClickedSquare(click, "all")
        break
    for i in blackpieces:
      if i.getLocation() == convertor1(clickedsquare):
        piece = i
    location = convertor1(clickedsquare)
    potential = piece.potential(location[0], location[1], positions)
    print(potential)
    newpotential = []
    for i in potential:
      print(i)
      newpotential.append(convertor2(i))
    gui.squareActivate(newpotential)
    gui.squareHighlight(newpotential)
    click2 = gui.getClick()
    potentialsquares = gui.locationsToSquareList(newpotential)
    if gui.checkSquareClick(click2, potentialsquares) == True:
      squaremoved = gui.getClickedSquare(click2, potentialsquares)
      gui.unhighlightAll()
      piecetype = piece.getType()
      piececolor = piece.getColor()
      movepiece = piececolor + piecetype
      piece.movement(convertor1(squaremoved))
      for i in positions:
        if convertor1(squaremoved) == i and positions[i] == "white":
          gui.eatMove(movepiece, convertor2(location), convertor2(convertor1(squaremoved)))
          moveMade = True
        else:
          gui.move(movepiece, convertor2(location),convertor2(convertor1(squaremoved)))
          moveMade = True

  #get mouse click to select square to move to
  #check if eat (to determine gui.move or gui.eatMove)
  #check if check or checkmate
  #move & redraw relevant squares
  #display move message


def main():
  #queen = Queen(2, 3, "white")
  #print("HI")
  #movelist = queen.potential(5, 5, {(3, 2): "black"})
  pawn1w = Pawn(1, 2, "white")
  pawn2w = Pawn(2, 2, "white")
  pawn3w = Pawn(3, 2, "white")
  pawn4w = Pawn(4, 2, "white")
  pawn5w = Pawn(5, 2, "white")
  pawn6w = Pawn(6, 2, "white")
  pawn7w = Pawn(7, 2, "white")
  pawn8w = Pawn(8, 2, "white")
  pawn1b = Pawn(1, 7, "black")
  pawn2b = Pawn(2, 7, "black")
  pawn3b = Pawn(3, 7, "black")
  pawn4b = Pawn(4, 7, "black")
  pawn5b = Pawn(5, 7, "black")
  pawn6b = Pawn(6, 7, "black")
  pawn7b = Pawn(7, 7, "black")
  pawn8b = Pawn(8, 7, "black")
  bishop1w = Bishop(3, 1, "white")
  bishop2w = Bishop(6, 1, "white")
  bishop1b = Bishop(3, 8, "black")
  bishop2b = Bishop(6, 8, "black")
  knight1w = Knight(2, 1, "white")
  knight2w = Knight(7, 1, "white")
  knight1b = Knight(2, 8, "black")
  knight2b = Knight(7, 8, "black")
  rook1w = Rook(1, 1, "white")
  rook2w = Rook(8, 1, "white")
  rook1b = Rook(1, 8, "black")
  rook2b = Rook(8, 8, "black")
  kingw = King(4, 1, "white")
  kingb = King(4, 8, "black")
  queenw = Queen(5, 1, "white")
  queenb = Queen(5, 8, "black")

  piecesw = [
    pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w, bishop1w,
    bishop2w, rook1w, rook2w, kingw, queenw, knight1w, knight2w
  ]

  piecesb = [
    pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b, bishop1b,
    bishop2b, rook1b, rook2b, kingb, queenb, knight1b, knight2b
  ]
  piecesblocation = []
  for i in piecesb:
    locb = i.getLocation()
    piecesblocation.append(locb)

  pieceswlocation = []
  for i in piecesw:
    locw = i.getLocation()
    pieceswlocation.append(locw)

  pieces = piecesb + piecesw

  gui = ChessGUI()
  #gui.squareHighlight(movelist)
  gui.setBoard()
  gameOver = False
  while gameOver == False:
    whiteTurn(gui, pieceswlocation, piecesw, makepositions(pieces))
    blackTurn(gui, piecesblocation, piecesb, makepositions(pieces))


main()
