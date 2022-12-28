def sudoku(puzzle):

    def find_next_empty_cell(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(puzzle, i, j, num):
        # Check row
        for k in range(9):
            if puzzle[i][k] == num:
                return False

        # Check column
        for k in range(9):
            if puzzle[k][j] == num:
                return False

        # Check 3x3 grid
        grid_x = i // 3
        grid_y = j // 3
        for k in range(3):
            for l in range(3):
                if puzzle[grid_x * 3 + k][grid_y * 3 + l] == num:
                    return False

        return True

    def solve(puzzle):
        next_empty_cell = find_next_empty_cell(puzzle)
        if not next_empty_cell:
            return True
        else:
            i, j = next_empty_cell

        for num in range(1, 10):
            if is_valid(puzzle, i, j, num):
                puzzle[i][j] = num
                if solve(puzzle):
                    return True
                puzzle[i][j] = 0

        return False

    solve(puzzle)
    return puzzle
