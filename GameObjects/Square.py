# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:04:19 2018

@author: Student
"""

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