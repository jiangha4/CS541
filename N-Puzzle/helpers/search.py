from helpers.grid import three_Grid, four_Grid
from helpers.node import Node
from helpers.myheapq import MyHeapQueue
import math


def check_goal(grid1, grid2):
    if grid1.grid == grid2.grid:
        return True
    return False


def check_parity(grid1, grid2):
    if (grid1.parity%2) == (grid2.parity%2):
        print("Parity is the same")
        return True
    print("Parity is different")
    return False


def backtrack(node):
    buf = []
    while node != None:
        buf.append(node)
        node = node.parent

    buf.reverse()
    steps = 0
    for node in buf:
        steps = steps + 1
        print(node)
    print("Number of steps = {}".format(steps))
    return steps


def misplaced_square_heuristic(current, goal):
    num = 0
    for i in range(0, len(current.grid)):
        if current.grid[i] == 'b':
            continue
        if current.grid[i] != goal.grid[i]:
            num = num + 1
    return num


threegrid_coordinates = [(0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 1), (1, 2),
                        (2, 0), (2, 1), (2, 2)]

fourgrid_coordinates = [(0, 0), (0, 1), (0, 2), (0, 3),
                        (1, 0), (1, 1), (1, 2), (1, 3),
                        (2, 0), (2, 1), (2, 2), (2, 3),
                        (3, 0), (3, 1), (3, 2), (3, 3)]

def manhattan_distance_heuristic(current, goal):
    if isinstance(goal, four_Grid):
        coordinates = fourgrid_coordinates
    else:
        coordinates = threegrid_coordinates
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
    if isinstance(goal, four_Grid):
        coordinates = fourgrid_coordinates
    else:
        coordinates = threegrid_coordinates
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


def generate_successors(node, queue, heur_function, goal_grid, astar=False):
    for state in node.action:
        if isinstance(goal_grid, four_Grid):
            newGrid = four_Grid(state)
        else:
            newGrid = three_Grid(state)
        depth = node.depth + 1
        if astar:
            heur = heur_function(newGrid, goal_grid) + depth
        else:
            heur = heur_function(newGrid, goal_grid)
        newNode = Node(newGrid, node, heur, depth)
        if check_goal(newGrid, goal_grid):
            return newNode
        queue.push(newNode)


def best_first_search(start_grid, heur_function, goal_grid):
    heur = heur_function(start_grid, goal_grid)
    starter_node = Node(start_grid, None, int(heur), 0)
    queue = MyHeapQueue()
    queue.push(starter_node)
    while not queue.isEmpty():
        curr = queue.pop()
        goal = generate_successors(curr, queue, heur_function, goal_grid)
        if goal:
            return goal
    return None


def a_star_search(start_grid, heur_function, goal_grid):
    heur = heur_function(start_grid, goal_grid)
    starter_node = Node(start_grid, None, int(heur), 0)
    queue = MyHeapQueue()
    queue.push(starter_node)
    while not queue.isEmpty():
        curr = queue.pop()
        goal = generate_successors(curr, queue, heur_function, goal_grid, True)
        if goal:
            return goal
    return None

if __name__ == '__main__':
    pass


