def check_parity(grid1, grid2):
    if (grid1.parity%2) == (grid2.parity%2):
        print("Parity is the same")
        return True
    print("Parity is different")
    return False


def misplaced_square_heuristic(current, goal):
    num = 0
    for i in range(0, len(current.grid)):
        if current.grid[i] == 'b':
            continue
        if current.grid[i] != goal.grid[i]:
            num = num + 1
    return num


def manhattan_distance_heuristic(current, goal):
    pass
