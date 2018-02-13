# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:04:19 2018

@author: Student
"""
import pygame

class Square:
    def __init__(self, x, y):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.owner = "unOwned"
        self.x = x
        self.y = y
    
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
        #implement here
      
    def drawRight(self, color):
        #implement here
          
    def drawTop(self, color):
        #implement here
      
    def drawBottom(self, color):
        #implement here
        
    def draw(self):
        fillBox = 0
        if(getLeft):
            self.drawLeft()
            fillBox +=1
        if(getRight):
            self.drawRight()
            fillBox +=1
        if(getTop):
            self.drawTop()
            fillBox +=1
        if(getBottom):
            self.drawBottom()
            fillBox +=1
        if(fillBox == 4):
            #Draw box fill color based on owner of Square
        
    