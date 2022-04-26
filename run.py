def find_next_empty(puzzle):
    # find the next row, col on the puzzle that is empty - replace with 0
    # return row,col tuple (or(None, None) if there is none )
    # NB - 0-8 indices used here
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # if no spaces left in the puzzle. 


def is_valid(puzzle, guess, row, col):
    # if a valid guess returns True, otherwise False

    # test the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # test the columns
    # col_vals = []
    # for i in range(9):
        # col_vals.append(puzzle[i] [col])
    col_vals = [puzzle[i][col] for i in range(9)]  
    if guess in col_vals:
        return False

    # test each 3 x 3 matrix
    # find where each square starts
    row_start = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1,  8 // 3 = 2
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
          
    # if we get here, the checks pass, the guess may be valid so
    return True    


def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # sudoku is a list of lists, where each inner loost is a row in the sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1 : make a guess
    row, col = find_next_empty(puzzle)

    if row is None:  # if there are no spaces left
        return True

    # step 2 : if there is a place to put a number, make a guess between 1-9
    for guess in range(1, 10): 
        # range(1, 10) is 1- 9 inclusive
        # step 3: check if this is valid guess    
       if is_valid(puzzle, guess, row, col):
    # step 3.1 : if this is valid, then place that guess in  the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid  OR if the guess does not solve the puzzle, 
        # then we need to backtrack and try a new number
            puzzle[row][col] = 0   # reset guess

    # step 6: if none of the numbers that we try work, then this 
    # puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
            [0, 0, 0,  0, 0, 3,  1, 0, 4],
            [0, 2, 0,  0, 1, 7,  0, 9, 0],
            [3, 0, 0,  0, 0, 0,  0, 5, 0],

            [0, 0, 8,  0, 2, 4,  0, 0, 0],
            [4, 0, 0,  0, 0, 0,  0, 0, 2],
            [0, 0, 0,  7, 0, 0,  3, 0, 0],

            [0, 5, 0,  0, 0, 0,  0, 0, 1],
            [0, 6, 0,  5, 8, 0,  0, 3, 0],
            [8, 0, 7,  6, 0, 0,  0, 0, 5]
        ] 
    print(solve_sudoku(example_board))
    print(example_board)

   