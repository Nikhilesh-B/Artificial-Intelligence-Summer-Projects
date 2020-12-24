#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:21:23 2020

@author: Nick
"""

import random
from BaseAI import BaseAI
from Grid import * 
from Displayer import Displayer
import numpy as np 

import time



class IntelligentAgent(BaseAI):
    
    def getMove(self, grid): 
        if grid: 
                print("Heuristic Function")
                print(self.heuristic_function(grid))
        
        
        child, utl = self.Maximise(grid, -10**100, 10*100)
        
       
        self.depthsearch_max = 0  
        return child[0] 
        

    

    def __init__(self):
        self.depthsearch_max = 0 
        self.Displayer  = Displayer()
    
    
    
    def increment_depthsearch(self):
        self.depthsearch_max = self.depthsearch_max + 1
        
    
    
    
    def heuristic_function(self, grid):   
            no_freeCells = len(grid.getAvailableCells())
            max_tile =  grid.getMaxTile()
            gravity = self.gravityCheckTopLeft(grid)
            f  = no_freeCells + max_tile 
            return f
    
    
    def gravityCheckTopLeft(self, grid):
        up  = 99.81
        topvalue = grid.map[0][0]
        return up*topvalue
    
    
    
    def getMoves4Min(self, insert, grid): 
        val = insert 
        possiblegrids = []
        gridduplicate = grid.clone()
        for x in range(0,4):
            for y in range(0,4):
                    grid.insertTile((x,y),val)
                    possiblegrids.append(grid.clone())
                    grid = gridduplicate

        return possiblegrids
        
    

    
    def Minimize(self, insert, grid, alpha, beta):
        if (self.depthsearch_max>4 or not grid.canMove()):                                         
            return None, self.heuristic_function(grid)
        
      
    
        (minChild, minUtility) = None, 10*100
        
        
        
        ##minimize is not making the move it's placing it where it needs to be placed so this is where the grid_instance must change 
        
        for grid_instance in self.getMoves4Min(insert, grid): 
            if(insert==2): 
                self.increment_depthsearch()
            
         

            y, utility = self.Maximise(grid_instance, alpha, beta)
            
            if utility < minUtility: 
                minChild, minUtility = grid_instance, utility 
        
            if minUtility <= alpha: 
                break
            
            if minUtility < beta: 
                beta = minUtility             
                
            return (minChild, minUtility)
       
    
    
    
    
    def Maximise(self, grid, alpha, beta): 
         if(self.depthsearch_max>4 or not grid.canMove()):  
      
             return None, self.heuristic_function(grid)
        
         
         (maxChild, maxUtility) = None, -10*1000
            
         for grid_instance in grid.getAvailableMoves():
            self.increment_depthsearch()
            a = (0.1*(self.Minimize(4, grid_instance[1], alpha, beta))[1])
            b = (0.9*(self.Minimize(2, grid_instance[1], alpha, beta))[1])
        
            utility  = a+b
            if utility > maxUtility: 
                maxChild, maxUtility =  grid_instance, utility 
            
            if maxUtility >= beta:
                break
            
            if maxUtility > alpha: 
                alpha = maxUtility 
        
         return (maxChild, maxUtility) 
    
    
    
    
    
    

   

 


    


