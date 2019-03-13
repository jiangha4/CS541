import random

class square(object):
    walls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 20, 30, 40, 50, 60, 70, 80, 90,
            19, 29, 39, 49, 59, 69, 79, 89, 99,
            90, 91, 92, 93, 94, 95, 96, 97, 98]

    def __init__(self, id, can):
        self.contains_can = can
        self.id = id

    def check_if_wall(self):
        if self.id in square.walls:
            return True
        return False

    def cleaned(self):
        self.contains_can = False

    def __repr__(self):
        return '[id: '+ str(self.id) + '/' + 'state: ' + str(self.contains_can) + ']'


def create_can():
    rand = random.randint(1, 1000)
    if rand%2 == 0:
        return True
    return False


def make_grid():
    robot_world = []
    for i in range(0, 100):
        robot_world.append(square(i, create_can()))
    return robot_world
