

from __future__ import division
from __future__ import print_function

import sys
import math
import time
from collections import deque 
from queue import PriorityQueue



class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] 		represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->stringx
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def getAction(self):
        return self.action

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[self.n*i : self.n*(i+1)])

    def move_up(self):
        n1  = self.n
        w = self.cost
        x  = list(self.config)
        idx_empty  = x.index(0)
        idx_swap = idx_empty-n1
        if(idx_empty<n1):
            return None
        else:
            x[idx_empty], x[idx_swap] = x[idx_swap], x[idx_empty]
            return PuzzleState(x,n1,self,"Up",w+1)        
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """

      
    def move_down(self):
        n1  = self.n
        w = self.cost
        x  = list(self.config)
        idx_empty  = x.index(0)
        idx_swap = idx_empty+n1
        if(idx_empty>=n1*(n1-1)):
            return None
        else:
            x[idx_empty], x[idx_swap] = x[idx_swap], x[idx_empty]
            return PuzzleState(x,n1,self,"Down",w+1)
        
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
      
    def move_left(self):
        n1  = self.n
        w  = self.cost
        x  = list(self.config)
        idx_empty  = x.index(0)
        idx_swap = idx_empty-1
        if(idx_empty%n1==0):
            return None
        else:
            x[idx_empty], x[idx_swap] = x[idx_swap], x[idx_empty]
            return PuzzleState(x,n1,self,"Left",w+1)
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """


    def move_right(self):
        n1  =self.n
        w = self.cost 
        x  = list(self.config)
        idx_empty  = x.index(0)
        idx_swap = idx_empty+1
        
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        if(idx_empty%n1==(n1-1)):
            return None
        else:
            x[idx_empty], x[idx_swap] = x[idx_swap], x[idx_empty]
            return PuzzleState(x,n1,self,"Right",w+1)
      
    def expand(self):
        """ Generate the child nodes of this node """
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children

        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]
        
        

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children



    def getConfig(self):
        return self.config
    
    def getCost(self):
        return self.cost
    
    def getParent(self):
        return self.parent
    
    def getN(self): 
        return self.n









def writeOutput(path_to_goal,cost_of_path,nodes_expanded,search_depth,max_search_depth):
    with open("ouput.txt","w") as f: 
        f.write("path_to_goal: "+str(path_to_goal)+'\n')
        f.write("cost_of_path: "+str(cost_of_path)+'\n')
        f.write("nodes_expanded: "+str(nodes_expanded)+'\n')
        f.write("search_depth: "+str(search_depth)+'\n')
        f.write("max_search_depth: "+str(max_search_depth)+'\n')
        f.close()
    


class BFS_queue(object):
    def __init__(self):
        self.q  = deque()
        
    def enqueue(self,x):
        self.q.append(x)

    def dequeue(self):
        return self.q.popleft()

    def contains(self,x):
        return (x in self.q)

    def getList(self):
        return list(self.q)

    def isEmpty(self):
        return(len(self.q)==0)


def bfs_search(initial_state):
    """BFS search"""
    frontier =  BFS_queue()
    frontier.enqueue(initial_state)
    frontierSet = set()
    frontierSet.add(tuple(initial_state.getConfig()))
    explored = set()
    nodes_expanded = 0 
    max_search_depth = 0
    path = []

    ##use a set for this 

    ## max-depth => you have the move-up and  move-down
    ## max-depth variable that starts of 0 that keeps track of the cost of the child

    ## nodes-expanded => keeping a total of how many nodes you've expanded, if you have expanded them 
           
    while not frontier.isEmpty():
        curr_state = frontier.dequeue()
        explored.add(tuple(curr_state.getConfig()))
        
        
        if (test_goal(curr_state)):
            print("breaking where we need to break")
            print("--------> Solved")
            curr_state.display()
            print(nodes_expanded)
            cost_of_path = curr_state.getCost()
            search_depth = cost_of_path
            print(cost_of_path)
            print(max_search_depth)
            while (curr_state.getParent()!=None):
                path.append(curr_state.getAction())
                curr_state = curr_state.getParent()
            path = path[::-1]
            print(path)
            writeOutput(path,cost_of_path,nodes_expanded,search_depth,max_search_depth)
            break
        
        children =  curr_state.expand()
        nodes_expanded = nodes_expanded+1
        for child in children:         ##that's correct                                     
            if tuple(child.getConfig()) not in explored and tuple(child.getConfig()) not in frontierSet:     ##this is the problem we have to fix up the cost is different so we can't make that comparison 
                frontier.enqueue(child)
                frontierSet.add(tuple(child.getConfig()))
                if(max_search_depth<child.getCost()):
                    max_search_depth = child.getCost()
        
        
        
        
        
class DFS_stack(object):
    def __init__(self):
        self.q  = []
        
    def push(self,x):
        self.q.append(x)

    def pop(self):
        return self.q.pop()

    def contains(self,x):
        return (x in self.q)

    def getList(self):
        return list(self.q)

    def isEmpty(self):
        return(len(self.q)==0)

    def length(self):
        return(len(self.q))
    def show(self):
        print(self.q)


    

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    frontier =  DFS_stack()
    frontier.push(initial_state)
    frontierSet = set()
    frontierSet.add(tuple(initial_state.getConfig()))
    explored = set()
    nodes_expanded = 0 
    max_search_depth = 0
    path = []
    
    ##use a set for this 

    ## max-depth => you have the move-up and  move-down
    ## max-depth variable that starts of 0 that keeps track of the cost of the child

    ## nodes-expanded => keeping a total of how many nodes you've expanded, if you have expanded them 
           
    while not frontier.isEmpty():
        curr_state = frontier.pop()
        frontierSet.remove(tuple(curr_state.getConfig()))
        explored.add(tuple(curr_state.getConfig()))
        
        
        if (test_goal(curr_state)):
            print("breaking where we need to break")
            print("--------> Solved")
            curr_state.display()
            print("Nodes expanded:")
            print(nodes_expanded)
            cost_of_path = curr_state.getCost()
            search_depth = cost_of_path
            print("Cost of Path:")
            print(cost_of_path)
            print("Max_Search_Depth:")
            print(max_search_depth)
            while (curr_state.getParent()!=None):
                path.append(curr_state.getAction())
                curr_state = curr_state.getParent()
            path = path[::-1]
            writeOutput(path,cost_of_path,nodes_expanded,search_depth,max_search_depth)
            break
        
        children =  curr_state.expand()[::-1]
        nodes_expanded = nodes_expanded+1
        
        for child in children:
            if tuple(child.getConfig()) not in explored and tuple(child.getConfig()) not in frontierSet:     ##this is the problem we have to fix up the cost is different so we can't make that comparison 
                
                frontier.push(child)
                frontierSet.add(tuple(child.getConfig()))
            
                if(max_search_depth<child.getCost()):
                    max_search_depth = child.getCost()








def A_star_search(initial_state):
    """A * search"""
    frontier  = PriorityQueue()
    
    
    frontierSet = set()
    explored =  set()
    frontierSet.add(tuple(initial_state.getConfig()))
    
    nodes_expanded=0
    max_search_depth = 0
    path = []
    count  = 0 
    
    frontier.put((calculate_total_cost(initial_state)+initial_state.getCost(),count,initial_state))
    
    while not frontier.empty():
        curr_state =  frontier.get()[2]
        explored.add(tuple(curr_state.getConfig()))
        
        
        if (test_goal(curr_state)):
            cost_of_path = curr_state.getCost()
            search_depth = cost_of_path
            curr_state.display()
            while (curr_state.getParent()!=None):
                path.append(curr_state.getAction())
                curr_state = curr_state.getParent()
            path = path[::-1]
            writeOutput(path,cost_of_path,nodes_expanded,search_depth,max_search_depth)
            break
    
        children = curr_state.expand()
        nodes_expanded = nodes_expanded+1
        for child in children:
            count = count + 1
            
            if tuple(child.getConfig()) not in explored and tuple(child.getConfig()) not in frontierSet:
                frontier.put((calculate_total_cost(child)+curr_state.getCost(),count,child))
                frontierSet.add(tuple(child.getConfig()))
                if(max_search_depth<child.getCost()):
                    max_search_depth = child.getCost()
                
            '''elif tuple(child.getConfig()) in frontierSet:
                frontier.put((calculate_total_cost(child)+child.getCost(),count,child))
                
                if(max_search_depth<child.getCost()):
                    max_search_depth = child.getCost()'''
        
                
      

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    total = 0
    config  = state.getConfig()
    for i in range(len(config)):
        if(config[i]!=0):
            total  =  total + calculate_manhattan_dist(i, config[i], state.getN())
    
    return total


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    idx = idx
    idx_y  = idx//n
    idx_x  = idx%n 
    x_prop = value%n
    y_prop = value//n 
    return abs(idx_y-y_prop)+abs(idx_x-x_prop)
    
    
    


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    config = puzzle_state.getConfig()
    return(config==sorted(config))



















import tracemalloc

##discrepancy when optimzing comparisons for new values i.e. we have a problem using a star with another comaprison in terms of the ast


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    tracemalloc.start()
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    


    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    
    with open("output.txt","a") as f: 
        f.write("running_time: "+str(end_time-start_time)+' s \n')
        f.write("max_ram_usage: "+str(peak/10**6)+" MB")
    
    
    
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()
