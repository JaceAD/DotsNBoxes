# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:04:19 2018

@author: Student
"""
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)

class Square:
    def __init__(self, x, y, surface):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.owner = "unOwned"
        self.x = x
        self.y = y
        self.surface = surface
        
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
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def getSide(self, sideChar):
        if(sideChar=="t"):
            return self.getTop()
        elif(sideChar=="b"):
            return self.getBottom()
        elif(sideChar=="l"):
            return self.getLeft()
        elif(sideChar=="r"):
            return self.getRight()
    
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
    
    def drawLeft(self, color):
        startX = self.getX()
        startY = self.getY()
        pygame.draw.line(self.surface, color, (startX, startY), (startX, startY + 100), 10)
      
    def drawRight(self, color):
        startX = self.getX() + 100
        startY = self.getY()
        pygame.draw.line(self.surface, color, (startX, startY), (startX, startY + 100), 10)
        #implement here
          
    def drawTop(self, color):
        startX = self.getX()
        startY = self.getY()
        pygame.draw.line(self.surface, color, (startX, startY), (startX + 100, startY), 10)
        #implement here
      
    def drawBottom(self, color):
        startX = self.getX()
        startY = self.getY() + 100
        pygame.draw.line(self.surface, color, (startX, startY), (startX + 100, startY), 10)
        #implement here
        
    def draw(self):
        if(self.getLeft()):
            self.drawLeft(BLACK)
        if(self.getRight()):
            self.drawRight(BLACK)
        if(self.getTop()):
            self.drawTop(BLACK)
        if(self.getBottom()):
            self.drawBottom(BLACK)
        if(self.getOwner() == "PlayerOne"):
            pygame.draw.rect(self.surface, BLUE, (self.getX(), self.getY(), 100, 100))
        elif (self.getOwner() == "PlayerTwo"):
            pygame.draw.rect(self.surface, RED, (self.getX(), self.getY(), 100, 100))
            #Draw box fill color based on owner of Square
        
    