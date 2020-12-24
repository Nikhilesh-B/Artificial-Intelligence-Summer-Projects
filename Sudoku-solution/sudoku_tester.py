#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:38:59 2020

@author: Nick
"""

from sudoku import * 


string='0006'  #I9 has to be 2
print(len(string))
board = { ROW[r] + COL[c]: int(string[9*r+c])
                      for r in range(9) for c in range(9)}

solved_board =  backtracking(board)
print_board(solved_board)


'''






'''
