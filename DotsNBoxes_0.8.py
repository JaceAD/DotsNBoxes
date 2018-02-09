# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:27:30 2018

@author: Student
"""

"""
Squares are based on the the number of sides taken, and if the number is equal to 4 then that player gets a point and gets to go again.
4 booleans for the sides
unclaimed, player 1 and player 2
squares in an array
int for number of squares done.
"""

import pygame
from GameObjects.Square import Square

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)

print("**Welcome To Dots and Boxes**")
print("")
print("You will be playing on an 8x8 grid of dots.")
print("Connect the dots that are next to each other to create a line.")
print("Be the last one to connect draw a line to form a box and earn 1 point.")
print("The player with the most Boxes wins.")
print("")


"""
numberSquaresComplete: is going to track the number of boxes owned by each player.
--playerOnePoints, playerTwoPoints: points are count on their respective counters below.--

isPlayerOne: is a bool simply to determine whose turn it is, and who gets the box once it is complete
continueTurn: a bool that will only activate when a player completes a square and gets to place another line
"""

########### Global Variables ###########
numberSquaresComplete = 0
playerOnePoints = 0
playerTwoPoints = 0
isPlayerOne = False #Will swap to true at start of first turn
continueTurn = False
board = []

dotRadius  = 10
boxWidth = 100
boxHeight = 100
boardOffsetX = 40
boardOffsetY = 40


width = 800
height = 800
screen = pygame.display.set_mode([width,height])

#Populates an 8 by 8 "board" 2D array with instances of Square
for i in range(0,5):
    tmpRow = []
    for j in range(0,5):
        tmpRow.append(Square())
    board.append(tmpRow)

def generateHorizontalXRanges():
    tmpList = []
    for i in range(0,5):
        tmpList.append([boardOffsetX + boxWidth*i + dotRadius, boardOffsetX + boxWidth*(i+1) - dotRadius])
    return tmpList
def generateHorizontalYRanges():
    tmpList = []
    for i in range(0,6):
        tmpList.append([i*boxHeight + boardOffsetY-dotRadius, i*boxHeight + boardOffsetY+dotRadius])
    return tmpList
def generateVerticalXRanges():
    tmpList = []
    for i in range(0,6):
        tmpList.append([i*boxWidth + boardOffsetX - dotRadius, i*boxWidth + boardOffsetX + dotRadius])
    return tmpList
def generateVerticalYRanges():
    tmpList = []
    for i in range(0,5):
        tmpList.append([boardOffsetY + dotRadius + i*boxHeight, boardOffsetY - dotRadius + (i+1) * boxWidth])
    return tmpList

horizontalXRanges = generateHorizontalXRanges()
horizontalYRanges = generateHorizontalYRanges()

verticalXRanges = generateVerticalXRanges()
verticalYRanges = generateVerticalYRanges()

########## Validation Functions ##########    

#Checks to see if cursor is over a side of a box
#Returns a list [rowIndex, columnIndex, sideChar] if it is, otherwise returns [-1,-1,n]
#User is responsible for handling error
def checkForSides(xCoord, yCoord):
    for i in range(0,5):
        if(xCoord >= horizontalXRanges[i][0] and xCoord <= horizontalXRanges[i][1]):
            for j in range(0,6):
                if(yCoord >= horizontalYRanges[j][0] and yCoord <= horizontalYRanges[j][1]):
                    if(j == 6):
                        return [j-1,i,"b"]
                    else:
                        return [j,i,"t"]
    for i in range(0,5):
        if(yCoord >= verticalYRanges[i][0] and yCoord <= verticalYRanges[i][1]):
            for j in range(0,6):
                if(xCoord >= verticalXRanges[j][0] and xCoord <= verticalXRanges[j][1]):
                    if(j == 6):
                        return [i,j,"r"]
                    else:
                        return [i,j,"l"]
    return [-1,-1,"n"]
                    
            
            
        

########## Draw Functions ##########
######### Draws the first Row of Boxes######
def drawFirstRow():
    #string for the first box in the upper left corner
    firstTopDots = " O    O"
    topRowDots = "    O"
    
    firstLeftRight = "     "
    firstRowMiddle = "     "
    
    firstBottomDots = "O    O"
    bottomLineDots = "    O"
    
    topLineArray = []
    leftRightArray = []
    bottomLineArray = []
    
    #draw top line first box
    if board[0][0].getTop() == True:
        firstTopDots = " O====O"
    else:
        firstTopDots = " O    O"
    topLineArray.append(firstTopDots)
    
    #draw top line of following boxes
    for i in range(7):
        if board[0][i+1].getTop() == True:
            topRowDots = "====O"
        else:
            topRowDots = "    O"
        topLineArray.append(topRowDots)
        
    #first box
    if board[0][0].getLeft() == True and board[0][0].getRight() == False:
        firstLeftRight = " |     "
    elif board[0][0].getLeft() == False and board[0][0].getRight() == True:
        firstLeftRight = "       |"
    elif board[0][0].getLeft() == True and board[0][0].getRight() == True:
        firstLeftRight = " |     |"
    else:
        firstLeftRight = "       "
    leftRightArray.append(firstLeftRight)
    
    #following boxes
    for i in range(7):
        if board[0][i+1].getRight() == True:
            firstRowMiddle = "    |"
        else:
            firstRowMiddle = "     "
        leftRightArray.append(firstRowMiddle)
    
    #draw bottom line first box
    if board[0][0].getBottom() == True:
        firstBottomDots = " O====O"
    else:
        firstBottomDots = " O    O"
    bottomLineArray.append(firstBottomDots)
    
    #draw bottom line of following boxes
    for j in range(7):
        if board[0][j+1].getBottom() == True:
            bottomLineDots = "====O"
        else:
            bottomLineDots = "    O"
        bottomLineArray.append(bottomLineDots)
        
    print(''.join(topLineArray))
    print(''.join(leftRightArray))
    print(''.join(bottomLineArray))
    del topLineArray[:]
    del leftRightArray[:]
    del bottomLineArray[:]
    return

####### Draw all boxes that are not on the first row ########
def drawLowerRows():
    
    firstLeftRight = "     "
    firstRowMiddle = "     "
    
    firstBottomDots = "O    O"
    bottomLineDots = "    O"
    
    lowerLeftRightArray = []
    lowerBottomLineArray = []
        
    for k in range(7):
        #first box
        if board[k+1][0].getLeft() == True and board[k+1][0].getRight() == False:
            firstLeftRight = " |     "
        elif board[k+1][0].getLeft() == False and board[k+1][0].getRight() == True:
            firstLeftRight = "       |"
        elif board[k+1][0].getLeft() == True and board[k+1][0].getRight() == True:
            firstLeftRight = " |     |"
        else:
            firstLeftRight = "       "
        lowerLeftRightArray.append(firstLeftRight)
        
        #following boxes
        for i in range(7):
            if board[k+1][i+1].getRight() == True:
                firstRowMiddle = "    |"
            else:
                firstRowMiddle = "     "
            lowerLeftRightArray.append(firstRowMiddle)
        
        #draw bottom line first box
        if board[k+1][0].getBottom() == True:
            firstBottomDots = " O====O"
        else:
            firstBottomDots = " O    O"
        lowerBottomLineArray.append(firstBottomDots)
        
        #draw bottom line of following boxes
        for j in range(7):
            if board[k+1][j+1].getBottom() == True:
                bottomLineDots = "====O"
            else:
                bottomLineDots = "    O"
            lowerBottomLineArray.append(bottomLineDots)

        print(''.join(lowerLeftRightArray))
        print(''.join(lowerBottomLineArray))
        
        del lowerLeftRightArray[:]
        del lowerBottomLineArray[:]
    return

########## State Update Functions ##########
#Updates a box after a move has been made
def updateBox(rowIndex, columnIndex, lineKey):
    #print("Inside update box. Update at index [",rowIndex,",",columnIndex,"] with lineKey:", lineKey)
    global board
    box = board[rowIndex][columnIndex]
    if(lineKey == "t"):
        box.setTop(True)
    elif(lineKey == "b"):
        box.setBottom(True)
    elif(lineKey == "l"):
        box.setLeft(True)
    elif(lineKey == "r"):
        box.setRight(True)
    if(box.getBottom() and box.getTop() and box.getLeft() and box.getRight()):
        global numberSquaresComplete
        if(isPlayerOne):
            box.setOwner("PlayerOne")
            global playerOnePoints
            playerOnePoints += 1
            numberSquaresComplete += 1
        else:
            box.setOwner("PlayerTwo")
            global playerTwoPoints 
            playerTwoPoints += 1
            numberSquaresComplete += 1
    board[rowIndex][columnIndex] = box
    
#Determines boxes to update after a move has been made and calls updateBox on them
#Input is the Row Index, Column Index, and char of side for the side a player clicked on
#Assumes input is valid
def updateBoard(rowIndex, columnIndex, lineChar):
    updateBox(rowIndex, columnIndex, lineChar)
    #If there's a box sharing a side with this one, update it too
    if(lineChar == "t" and rowIndex > 0):
        updateBox(rowIndex-1, columnIndex, "d")
    elif(lineChar == "b" and rowIndex < 7):
        updateBox(rowIndex+1, columnIndex, "t")
    elif(lineChar == "r" and columnIndex < 7):
        updateBox(rowIndex, columnIndex+1, "l")
    elif(lineChar == "l" and columnIndex > 0):
        updateBox(rowIndex, columnIndex-1, "r")

#Keeps player in control if they get another turn. Otherwise swaps to other player
def continueTurn(cont):
    if(not cont):
        #Swap if the player doesn't have another turn.
        global isPlayerOne
        isPlayerOne = not isPlayerOne

        
def drawBlackDots():
    global screen
    global dotRadius
    global boxWidth
    global boxHeight
    
    for i in range(7):
        for j in range(7):
            posX = int(boxWidth*i + boardOffsetX)
            posY = int(boxHeight*j + boardOffsetY)
            pygame.draw.circle(screen, BLACK, (posX, posY), dotRadius)

def main():
    pygame.init()
    
    global width
    global height
    global screen
    
   
    
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------\
    done = False
    while not done:
        # --- Main event loop
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: # If user clicked close
                done = True
        gameMouse = pygame.mouse
        posTuple = gameMouse.get_pos()
        textFont = pygame.font.Font(None, 36)
       
        
        # --- Drawing code should go here
        # First, clear the screen
        background_color = WHITE 
        screen.fill(background_color) 
        mousePosSurface = textFont.render("x: " + str(posTuple[0]) + " y: " + str(posTuple[1]), 0, BLUE)
        
        drawBlackDots()
        screen.blit(mousePosSurface, (5,5))
        # --- Update the screen with what we've drawn.
        pygame.display.update()
    
        # This limits the loop to 60 frames per second
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e