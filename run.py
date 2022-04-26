puzzle = [
    [6, 0, 8,  0, 0, 3,  0, 2, 0],
    [0, 4, 1,  0, 8, 0,  0, 0, 7],
    [0, 0, 0,  0, 4, 5,  9, 6, 0],

    [0, 1, 4,  0, 9, 0,  3, 0, 2],
    [0, 0, 0,  2, 0, 4,  0, 0, 0],
    [2, 0, 3,  0, 5, 0,  4, 7, 0],

    [0, 2, 9,  3, 1, 0,  0, 8, 5],
    [5, 0, 0,  0, 6, 0,  2, 0, 0],
    [0, 3, 0,  5, 0, 0,  0, 0, 9]
] 

def find_next_empty(puzzle):
    #find the next row, col on the puzzle that is empty - replace with 0
    # return row,col tuple (or(None, None) if there is none )
    # NB - 0-8 indices used here
    for r in range(9):
        for c in rang(9):
            if puzzle[r] [c] == 0:
                return r, c

    return None, None      # if no spaces left in the puzzle  

def is_valid(puzzle, guess, row, col):
    # if a valid guess returns True, otherwise False



def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # sudoku is a list of lists, where each inner loost is a row in the sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1 : make a guess
    row, col = find_next_empty(puzzle)

    if row is None: # if there are no spaces left
        return True

   #step 2 : if there is a place to put a number, make a guess between 1-9
   for guess in range(1,10): # range(1, 10) is 1- 9 inclusive 
       # step 3: check if this is valid guess    
       id is_valid(puzzle, guess, row, col):

