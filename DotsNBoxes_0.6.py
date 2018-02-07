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

#Square object. Contains booleans for if a side of it has been placed 
# and an owner String for the player that scored it.
class Square:
    def __init__(self):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.owner = "unOwned"
    
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getOwner(self):
        return self.owner
    
    def setLeft(self, leftBool):
        self.left = leftBool
    def setRight(self, rightBool):
        self.right = rightBool
    def setTop(self, topBool):
        self.top = topBool
    def setBottom(self, bottomBool):
        self.bottom = bottomBool    
    def setOwner(self, newOwner):
        self.owner = newOwner

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
#Populates an 8 by 8 "board" 2D array with instances of Square
board = []
for i in range(0,8):
    tmpRow = []
    for j in range(0,8):
        tmpRow.append(Square())
    board.append(tmpRow)


########### Utility Functions ##########
def convertRowInputToArrayCoordinate(rowVal):
    return rowVal - 97
def convertColumnInputToArrayCoordinate(columnVal):
    return columnVal-1


########## Validation Functions ##########
def validateCommand(rowVal, columnVal, lineVal):
    valid = True
    if not(rowInput >= 97 and rowInput <= 104):
        print("Invalid row used. Use a letter between a and h.")
        valid = False
    if not(columnInput >= 1 and columnInput <= 8):
        print("Invalid column used. Use a number between 1 and 8")
        valid = False
    if not(lineInput == 116 or lineInput == 98 or lineInput == 108 or lineInput == 114):
        print("Invalid line specified. Use \"t\" for Top, \"b\" for Bottom, \"l\" for Left, \"r\" for Right")
        valid = False
    return valid

    
def validateMove(rowVal, columnVal, lineVal):
    valid = True
    rowIndex = convertRowInputToArrayCoordinate(rowVal);
    columnIndex = convertColumnInputToArrayCoordinate(columnVal);
    #print("using rowIndex of ", rowIndex, "and column index of", columnIndex)
    tmpBox = board[rowIndex][columnIndex]
    if(lineInput == 116 and tmpBox.getTop()):
        valid = False
        print("Invalid move: that line is already drawn")
    elif(lineInput == 114 and tmpBox.getRight()):
        valid = False
        print("Invalid move: that line is already drawn")
    elif(lineInput == 108 and tmpBox.getLeft()):
        valid = False
        print("Invalid move: that line is already drawn")
    elif(lineInput == 98 and tmpBox.getBottom()):
        valid = False
        print("Invalid move: that line is already drawn")
    return valid
        

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

#####TESTING BOARD INITIALIZATION######
    """
tmpBox = board[0][0]
tmpBox.setTop(True)
for i in range(0,8):
    for j in range(0,8):
        print("box at",i,":",j,"has top equal to",str(board[i][j].getTop()))
        """
######END BOARD TESTING###########


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
def updateBoard(rowVal, columnVal, lineVal):
    #print("Inside updateBoard")
    rowIndex = convertRowInputToArrayCoordinate(rowVal)
    columnIndex = convertColumnInputToArrayCoordinate(columnVal)
    lineKey = chr(lineVal)
    #print("calling update box")
    updateBox(rowIndex, columnIndex, lineKey)
    #print("Checking for adjacent box")
    #If there's a box sharing a side with this one, update it too
    if(lineKey == "t" and rowIndex > 0):
        updateBox(rowIndex-1, columnIndex, "d")
    elif(lineKey == "b" and rowIndex < 7):
        updateBox(rowIndex+1, columnIndex, "t")
    elif(lineKey == "r" and columnIndex < 7):
        updateBox(rowIndex, columnIndex+1, "l")
    elif(lineKey == "l" and columnIndex > 0):
        updateBox(rowIndex, columnIndex-1, "r")

#Keeps player in control if they get another turn. Otherwise swaps to other player
def swapTurn(cont):
    if(not cont):
        #Swap if the player doesn't have another turn.
        global isPlayerOne
        isPlayerOne = not isPlayerOne

########### Main Game loop ###########
#Will still play the game until all boxes are filled

#while numberSquaresComplete < 64:
#    swapTurn(continueTurn)
#    continueTurn = False
#    
#    #Call Draw Function Here. Wipe screen before drawing?
#    drawFirstRow()
#    drawLowerRows()
#    
#    if isPlayerOne == True:
#        print("Player 1's Turn!")
#    else:
#        print("Player 2's Turn!")
#        
#    if isPlayerOne == True:
#        print("Player 1 please list a box you want to draw a line on.")
#    else:
#        print("Player 2 please list a box you want to draw a line on.")
#       
#    rowInput = None
#    columnInput = None
#    lineInput = None
#    
#    #Input validation loop. Will not exit until input passes validation conditions
#    while(True):
#        #2 Stage validation: First checks command is valid. Next checks that the move is possible.
#        while(True):
#            try:
#                rowInput = ord(input("For the Row Please use a lowercase letter between a - h:").lower())
#                columnInput = int(input("For the Column Please Enter a number between 1 - 8:"))
#                lineInput = ord(input("Enter t for Top, b for Bottom, l for Left, r for Right:"))
#                #print("rowInput was", str(rowInput), "columnInput was", str(columnInput), "lineInput was", str(lineInput))    
#                break
#            except TypeError:
#                print("please input only a single character of the specified type")
#        #Stage 1. Validates input is an acceptable command.
#        validInput = validateCommand(rowInput, columnInput, lineInput)
#    
#        if(validInput):
#            #Stage 2. Iff stage 1 is successful, validates the move can be made
#            validInput = validateMove(rowInput, columnInput, lineInput)
#            if(validInput): 
#                break #Iff both stages pass validation, leave input validation loop. Else loop for new input.
#        
#    updateBoard(rowInput,columnInput,lineInput)
#
        
def drawBlackDots():
    
        
WHITE = (255, 255, 255)

def main():
    pygame.init()
    
    width = 800
    height = 600
    screen = pygame.display.set_mode([width,height])
    
    clock = pygame.time.Clock()
    
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If user clicked close
                done = True
                
        background_color = WHITE 
        screen.fill(background_color) 
        
        pygame.display.update()
        
        clock.tick(60)
        
    pygame.quit

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e