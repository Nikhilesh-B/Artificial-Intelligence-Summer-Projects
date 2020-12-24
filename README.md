# Artificial-Intelligence-Summer-Projects
A repository of some interesting artificial intelligence summer projects I completed over the summer of 2020.

This repository contains the following direcotries and files: 

A) 8-puzzle solution (a direcotry of python files where I implement different graph searching methods including BFS, DFS and A* to solve the hardest sudoku problems):
     i) puzzle.py: implements BFS, DFS and A* to solve the 8-puzzle problem 
     ii) tester.py: takes in txt files as input of an incomplete sudoku board and outputs the solved sudoku boards into a another textfile. 

B) Sudoku solution (a direcotry of python files where I implement backtacking search to solve the sudoku challenge):
      i) sudoku_start.txt: a text file that contains all the unsolved sudoku boards where 0 represents an empty slot. 
      ii)sudoku_finish.txt: a text file that contains all the solved sudoku boards 
      iii)sudoku.py: implements BTS, and forward checking to solve a sudoku board. 
      iv) sudoku_tester.py: tests my sudoku.py solution, converting txt sudoku boards into matrices that are processed by sudoku.py 

C) 2048 solution (An intelligent agent that implements the expectiminimax algorithm with various heuristics to play the 2048 game):
      i) Dislayer.py: the displayer code that shows the board to the user 
      ii) BaseAI.py, ComputerAI.py: the code that drives the bot's actions in the game 
      iii) IntelligentAgent.py: the actual implementation of expectiminimax and heuristics. 

D) Perceptron learning algorithm (uses the PLA algorithm to make find a decision boundary between different points):
      i) PLA.py: the implementation of PLA that reads in a table, and implements the perceptron learning algorithm to find the solution required. 
 
E) Kmeans (uses the KMEANS algorithm to compress and image file down to an image file with various different colors):
      i) clustering.py: uses sklearn to classify pixels into different k-means buckets.

F) CNN (implements a convolutional neural network to classify hand sign images):
      i) sign_language.py

     
      
