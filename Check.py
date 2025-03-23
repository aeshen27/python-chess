#Check

def findCheck(x,y,positions):
    positionsblack = [(1,2): "black"
    kingwhiteposition = [4,1]
    check = False
    for i in pieces:
        if i.checking == True:
            check = True
    #checkmate
    checkmatecount = 0
    checkmate1 = False
    checkmateblocking = False
    checkmatefinal = False
    for i in positionsblack:
        if i.checking = True:
                for z in king.potential:
                    for r in positionsblack.potential:
                        if z == r:
                              checkmatecount +=1
                for x in i.potential():
                    for q in positionswhite:
                      if x == q:
                          checkmateblocking == True
    if checkmatecount == len(king.potential):
                      checkmate1 = True
    if checkmate1 and checkmateblocking:
        checkmatefinal = True
    if check:
      if check and checkmatefinal:
        return("checkmate")
      else:
        return("check")
        
    
                      
