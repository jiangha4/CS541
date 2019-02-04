import math

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


coordinates = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)]

def manhattan_distance_heuristic(current, goal):
    sum = 0
    for i in range(0, len(current.grid)):
        if current.grid[i] == 'b':
            continue
        if current.grid[i] != goal.grid[i]:
            x0, y0 = coordinates[i] # i is current location
            goal_location = goal.grid.index(current.grid[i])
            x1, y1 = coordinates[goal_location] # where this block should be
            sum = sum + (abs(x0 - x1) + abs(y0 - y1))
    return sum

def euclidean_distance_heuristic(current, goal):
    sum = 0
    for i in range(0, len(current.grid)):
        if current.grid[i] == 'b':
            continue
        if current.grid[i] != goal.grid[i]:
            x0, y0 = coordinates[i] # i is current location
            goal_location = goal.grid.index(current.grid[i])
            x1, y1 = coordinates[goal_location] # where this block should be
            a = (x0 - x1)**2
            b = (y0 - y1)**2
            sum = sum + math.sqrt(a+b)
    return round(sum)
