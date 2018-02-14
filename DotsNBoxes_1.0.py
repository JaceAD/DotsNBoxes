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
isPlayerOne = True #Will swap to true at start of first turn
contTurn = True
board = []

dotRadius  = 10
boxWidth = 100
boxHeight = 100
boardOffsetX = 40
boardOffsetY = 40


width = 800
height = 800
screen = pygame.display.set_mode([width,height])

#Populates a 6 by 6 "board" 2D array with instances of Square
for i in range(0,6):
    tmpRow = []
    for j in range(0,6):
        tmpX = boardOffsetX + j*boxWidth
        tmpY = boardOffsetY + i*boxHeight
        tmpRow.append(Square(tmpX, tmpY, screen))
    board.append(tmpRow)

def generateHorizontalXRanges():
    tmpList = []
    for i in range(0,6):
        tmpList.append([boardOffsetX + boxWidth*i + dotRadius, boardOffsetX + boxWidth*(i+1) - dotRadius])
    return tmpList
def generateHorizontalYRanges():
    tmpList = []
    for i in range(0,7):
        tmpList.append([i*boxHeight + boardOffsetY-dotRadius, i*boxHeight + boardOffsetY+dotRadius])
    return tmpList
def generateVerticalXRanges():
    tmpList = []
    for i in range(0,7):
        tmpList.append([i*boxWidth + boardOffsetX - dotRadius, i*boxWidth + boardOffsetX + dotRadius])
    return tmpList
def generateVerticalYRanges():
    tmpList = []
    for i in range(0,6):
        tmpList.append([boardOffsetY + dotRadius + i*boxHeight, boardOffsetY - dotRadius + (i+1) * boxWidth])
    return tmpList

horizontalXRanges = generateHorizontalXRanges()
horizontalYRanges = generateHorizontalYRanges()

verticalXRanges = generateVerticalXRanges()
verticalYRanges = generateVerticalYRanges()

#Keeps player in control if they get another turn. Otherwise swaps to other player
def continueTurn(cont):
    if(not cont):
        #Swap if the player doesn't have another turn.
        global isPlayerOne
        isPlayerOne = not isPlayerOne

#Checks to see if cursor is over a side of a box
#Returns a list [rowIndex, columnIndex, sideChar] if it is, otherwise returns [-1,-1,n]
#User is responsible for handling error
def checkForSides(xCoord, yCoord):
    for i in range(0,6):
        if(xCoord >= horizontalXRanges[i][0] and xCoord <= horizontalXRanges[i][1]):
            for j in range(0,7):
                if(yCoord >= horizontalYRanges[j][0] and yCoord <= horizontalYRanges[j][1]):
                    if(j == 6):
                        return [j-1,i,"b"]
                    else:
                        return [j,i,"t"]
    for i in range(0,6):
        if(yCoord >= verticalYRanges[i][0] and yCoord <= verticalYRanges[i][1]):
            for j in range(0,7):
                if(xCoord >= verticalXRanges[j][0] and xCoord <= verticalXRanges[j][1]):
                    if(j == 6):
                        return [i,j-1,"r"]
                    else:
                        return [i,j,"l"]
    return [-1,-1,"n"]

def highlightSide(posTuple):
    checkVal = checkForSides(posTuple[0], posTuple[1])
    if(not(checkVal[0] == -1)):
        try:
            if(checkVal[2] == "r"):
                if(not board[checkVal[0]][checkVal[1]].getRight()):
                    board[checkVal[0]][checkVal[1]].drawRight(BLUE)
            elif(checkVal[2] == "l"):
                if(not board[checkVal[0]][checkVal[1]].getLeft()):
                    board[checkVal[0]][checkVal[1]].drawLeft(BLUE)
            elif(checkVal[2] == "t"):
                if(not board[checkVal[0]][checkVal[1]].getTop()):
                    board[checkVal[0]][checkVal[1]].drawTop(BLUE)
            elif(checkVal[2] == "b"):
                if(not board[checkVal[0]][checkVal[1]].getBottom()):
                    board[checkVal[0]][checkVal[1]].drawBottom(BLUE)
            else:
                raise Exception("Invalid mouse position being processed. Row: " + checkVal[0] + 
                                " column: " + checkVal[1] + " side key: " + checkVal[2])
        except:
            print("Error. Row: " + str(checkVal[0]) + " column: " + str(checkVal[1]) + " side key: " + checkVal[2])

########## State Update Functions ##########
#Updates a box after a move has been made
def updateBox(rowIndex, columnIndex, lineKey):
    print("Inside update box. Update at index [",rowIndex,",",columnIndex,"] with lineKey:", lineKey)
    global board
    global contTurn
    box = board[rowIndex][columnIndex]
    if(lineKey == "t"):
        if(not box.getTop()):
            box.setTop(True)
            contTurn = False
    elif(lineKey == "b"):
         if(not box.getBottom()):
             box.setBottom(True)
             contTurn = False
    elif(lineKey == "l"):
         if(not box.getLeft()):
             box.setLeft(True)
             contTurn = False
    elif(lineKey == "r"):
         if(not box.getRight()):
             box.setRight(True)
             contTurn = False
    if(box.getBottom() and box.getTop() and box.getLeft() and box.getRight()):
        global numberSquaresComplete
        if(isPlayerOne):
            box.setOwner("PlayerOne")
            global playerOnePoints
            playerOnePoints += 1
            print("player 1 scored")
            numberSquaresComplete += 1
        else:
            box.setOwner("PlayerTwo")
            global playerTwoPoints 
            playerTwoPoints += 1
            print("player 2 scored")
            numberSquaresComplete += 1
    print(box.getOwner())
#Determines boxes to update after a move has been made and calls updateBox on them
#Input is the Row Index, Column Index, and char of side for the side a player clicked on
#Assumes input is valid
def updateBoard(rowIndex, columnIndex, lineChar):
    print("Updating board")
    tmpPoints1 = playerOnePoints
    tmpPoints2 = playerTwoPoints
    print("player1:", str(tmpPoints1), "player2:", str(tmpPoints2))
    if(not board[rowIndex][columnIndex].getSide(lineChar)):
        updateBox(rowIndex, columnIndex, lineChar)
        #If there's a box sharing a side with this one, update it too
        if(lineChar == "t" and rowIndex > 0):
            print("updating above box")
            updateBox(rowIndex-1, columnIndex, "b")
        elif(lineChar == "b" and rowIndex < 5):
            print("updating below box")
            updateBox(rowIndex+1, columnIndex, "t")
        elif(lineChar == "r" and columnIndex < 5):
            print("updating right box")
            updateBox(rowIndex, columnIndex+1, "l")
        elif(lineChar == "l" and columnIndex > 0):
            print("updating left box")
            updateBox(rowIndex, columnIndex-1, "r")
        print("player1:", str(tmpPoints1), "player2:", str(tmpPoints2))
        print("player1Glob:", str(playerOnePoints), "player2Glob:", str(playerTwoPoints))
    if(tmpPoints1 < playerOnePoints or tmpPoints2 < playerTwoPoints):
        global contTurn
        contTurn = True
    continueTurn(contTurn)
    contTurn = True
    
def inputMove(positionTuple):
    checkVal = checkForSides(positionTuple[0], positionTuple[1])
    if(not(checkVal[0] == -1)):
        updateBoard(checkVal[0], checkVal[1], checkVal[2])
        
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
    textFont = pygame.font.Font(None, 36)
    processingInput = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------\
    done = False
    
    while not done:
        gameMouse = pygame.mouse
        posTuple = gameMouse.get_pos()
        
        # --- Main event loop
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(not processingInput):
                    processingInput = True
                    inputMove(posTuple)
                    processingInput = False
            
            textFont = pygame.font.Font(None, 36)
            # --- Drawing code should go here
            # First, clear the screen
            background_color = WHITE 
            screen.fill(background_color)
            
            #Graphical rendering to perform while game is still going
        if(numberSquaresComplete < 36):
             
            mousePosSurface = textFont.render("x: " + str(posTuple[0]) + " y: " + str(posTuple[1]), 0, BLUE)
            playerString = ""
            if(isPlayerOne):
                playerString = "Player One"
            else:
                playerString = "Player Two"
            playerString += "'s Turn!"    
            playerTurnSurface = textFont.render(playerString,0,BLACK)
            score1Surface = textFont.render("Player 1: " + str(playerOnePoints) + " points", 0, BLACK)
            score2Surface = textFont.render("Player 2: " + str(playerTwoPoints) + " points", 0, BLACK)
            drawBlackDots()
            
            highlightSide(posTuple)
            
            for i in range(0,6):
                for j in range(0,6):
                    board[i][j].draw()
                    
            screen.blit(mousePosSurface, (5,5))
            screen.blit(playerTurnSurface, (300, 700))
            
        else:
            winner = ""
            if(playerOnePoints > playerTwoPoints):
                winner = "player 1 wins!"
            elif(playerOnePoints < playerTwoPoints):
                winner = "player 2 wins!"
            else:
                winner = "Tie!"
            winnerSurface = textFont.render(winner,0,BLACK)
            screen.blit(winnerSurface, (330,300))
            
        screen.blit(score1Surface, (100, 750))
        screen.blit(score2Surface, (500, 750))
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