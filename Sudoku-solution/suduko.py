
import sys
import time
import numpy
import statistics
"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


order_of_selection = [1,2,3,4,5,6,7,8,9]

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    ##implementing this with reference to MRV 
    ##also with forward checking 
    if assignmentComplete(board) == True:
        solved_board = board 
        return solved_board
    

    
    else:
        var, domains = select_MRV(board)
        domain =  domains[var]
         
         
        ##now using propogation to check the values 
        
        
        ## now implementing forward checking has no legal values 
        
        ## we need to go through and check if appplying a particular variable leads to no possible variables for the correct columns, rows and squares
        new_domain = domain
            
        ##go through and select the correct value for the var 
        for value in new_domain: 
            
            if check_valid_insert(board, var, value) == True:
                board[var] = value 
                result =  backtracking(board)
                
                if result != "Failure":
                    return result
                board[var] = 0
        
        return "Failure"
  
    
  
    
  
def FC(var, board, domain): 
    ##we need to check if there is no valid inserts for entries in the same columns and the same rows 
    ##checking in the same column
    x = [1,2,3,4,5,6,7,8,9]
    board2 = board 
    for d in domain: 
        board2[var] = d
        print_board(board2)

        column_value = var[1]
        for j in range(len(ROW)):
            key2 = ROW[j]+column_value 
            print(key2)
            if board2[key2] == 0: 
                count = 0 
                for value in domain:
                    if(not check_valid_insert(board2, var, value)):
                        count = count + 1
                        if count == len(domain):
                            domain.remove(d)
                            print("activated")
        
        print("AAAAAA")
        row_value = var[0]
        for j in range(len(ROW)):
            key2 = row_value+COL[j]
            print(key2)
            if board2[key2] == 0: 
                count1 = 0 
                for value in x:
                    if(not check_valid_insert(board2, var, value)):
                        count1 = count1 + 1
                        if count1 == 9:
                            domain.remove(d)   
                            print("activated 2")
        
        square1 = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
        square2 = ["A4","B4","C4","A5","B5","C5","A6","B6","C6"]
        square3 = ["A7","B7","C7","A8","B8","C8","A9","B9","C9"]
        square4 = ["D1","E1","F1","D2","E2","F2","D3","E3","F3"]
        square5 = ["D4","E4","F4","D5","E5","F5","D6","E6","F6"]
        square6 = ["D7","E7","F7","D8","E8","F8","D9","E9","F9"]
        square7 = ["G1","H1","I1","G2","H2","I2","G3","H3","I3"]
        square8 = ["G4","H4","I4","G5","H5","I5","G6","H6","I6"]
        square9 = ["G7","H7","I7","G8","H8","I8","G9","H9","I9"]
        matrix  = [square1,square2,square3,square4,square5,square6,square7,square8,square9]
        
        for square in matrix: 
            if var in square: 
                for key2 in square:
                    if board2[key2] == 0:
                        count2 = 0
                        for value in x: 
                            if(not check_valid_insert(board2, var, value)):
                                count2 = count2 + 1
                                if count2 == 9:
                                    domain.remove(d)  
                                    print("activated 3")
                    
    return domain
    

    
    
    
    
    

def select_MRV(board):
    minimum_remaining_value = "filler"
    values = [1,2,3,4,5,6,7,8,9]
    count = 0 
    
    ledger = dict()
    domains = dict()
    
    for key in board: 
        domain = []
        if board[key] == 0: 
            for value in values: 
                if(check_valid_insert(board, key, value)):
                    count = count+1
                    domain.append(value)
            domains[key] = domain
            ledger[key] = count 
        count = 0
    
    return min(ledger, key=ledger.get), domains 
    
    
            
       


def check_valid_insert(board, key, value):
    if check_columns_valid(board, key, value) and check_rows_valid(board, key, value) and squares_valid(board, key, value): 
        return True
    
    else:
        return False


def check_columns_valid(board, key, value):
    column_value = key[1]
    boolean = True
    for j in range(len(ROW)):
        key2 = ROW[j]+column_value 
        if board[key2] == value: 
            boolean = False
            break
    return boolean 
        

    
def check_rows_valid(board, key, value ): 
    row_value = key[0]
    boolean = True
    for j in range(len(COL)):
        key2 = row_value+COL[j]
        if board[key2] == value: 
            boolean = False
            break
    return boolean 
        
    
    
def squares_valid(board, key, value): 
    boolean = True
    square1 = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
    square2 = ["A4","B4","C4","A5","B5","C5","A6","B6","C6"]
    square3 = ["A7","B7","C7","A8","B8","C8","A9","B9","C9"]
    square4 = ["D1","E1","F1","D2","E2","F2","D3","E3","F3"]
    square5 = ["D4","E4","F4","D5","E5","F5","D6","E6","F6"]
    square6 = ["D7","E7","F7","D8","E8","F8","D9","E9","F9"]
    square7 = ["G1","H1","I1","G2","H2","I2","G3","H3","I3"]
    square8 = ["G4","H4","I4","G5","H5","I5","G6","H6","I6"]
    square9 = ["G7","H7","I7","G8","H8","I8","G9","H9","I9"]
    matrix  = [square1,square2,square3,square4,square5,square6,square7,square8,square9]
    
    for square in matrix: 
        if key in square: 
            for key2 in square: 
                if board[key2] == value:
                    boolean = False
                    break 
    
    return boolean 
        
    


def assignmentComplete(board): 
    boolean = True
    for key in board: 
        if int(board[key]) == 0:
            boolean = False 
    
    return boolean 

    

def allDif(integer, lst): 
        if integer in lst: 
            return False
        else: 
            return True





if __name__ == '__main__':

    if len(sys.argv) > 1:

        #  Read individual board from command line arg.
        sudoku = sys.argv[1]

        if len(sudoku) != 81:
            print("Error reading the sudoku string %s" % sys.argv[1])
        else:
            board = { ROW[r] + COL[c]: int(sudoku[9*r+c])
                      for r in range(9) for c in range(9)}
            
            print_board(board)

            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()

            print_board(solved_board)

            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

    else:

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        print("trying")
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        times = []
        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                    for r in range(9) for c in range(9)}

            # Print starting board.
            print_board(board)

            # Solve with backtracking
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            times.append(end_time-start_time)
            # Print solved board. 
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')
        
        
        print("Finishing all boards in file.")
        print("Min:"+str(min(times)))
        print("Min:"+str(max(times)))
        print("Std_dev:"+str(statistics.stdev(times)))
        print("Mean:"+str(statistics.mean(times)))
        
