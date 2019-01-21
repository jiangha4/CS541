import random
import logging
from logger import Logger
from statistics import mean
import argparse

class girdSlot(object):
    def __init__(self, id, state):
        self.state = state
        self.id = id

    def clean(self):
        self.state = 'clean'

    def dirty(self):
        self.state = 'dirty'

    def __repr__(self):
        return '[id: '+ str(self.id) + '/' + 'state: ' + self.state + ']'

class vaccumWorld(object):
    def __init__(self, numPiles):
        self.piles = numPiles
        self.randomLocations = self.generateRandomNumbers()
        self.grid = self.createGrid()

    def generateRandomNumbers(self):
        randomLocations = list()
        for x in range(0, self.piles):
            rand = random.randint(0, 9)
            while rand in randomLocations:
                rand = random.randint(0, 9)
            randomLocations.append(rand)
        return randomLocations

    def createSquare(self, id, state):
        square = girdSlot(id, state)
        return square

    def createGrid(self):
        row = list()
        for i in range(0, 9):
            if i in self.randomLocations:
                row.append(self.createSquare(i, 'dirty'))
            else:
                row.append(self.createSquare(i, 'clean'))
        return row

class robot(object):
    topEdge = [0, 1, 2]
    leftEdge = [0, 3, 6]
    rightEdge = [2, 4, 8]
    botEdge = [6, 7, 8]

    actionMap = ['right', 'right', 'down', 'down', 'left', 'left','right','right', 'start']

    randomActionMap = ['up', 'down', 'left', 'right', 'suck', 'nothing']

    def __init__(self, start_location, randomAgent=None):
        if randomAgent:
            self.location = random.randint(0, 8)
        else:
            self.location = start_location
        self.performanceMeasure = 0
        self._logger = Logger(self.__class__.__name__).get()
        self._logger.debug("Robot init at: {}".format(self.location))

    def moveLeft(self):
        if self.location not in robot.leftEdge:
            self.location = self.location - 1
            self._logger.debug("Robot has moved left. At: {}".format(self.location))
            return True
        self._logger.debug("Robot can't move left")
        return False

    def moveRight(self):
        if self.location not in robot.rightEdge:
            self.location = self.location + 1
            self._logger.debug("Robot has moved right. At: {}".format(self.location))
            return True
        self._logger.debug("Robot can't move right")
        return False

    def moveUp(self):
        if self.location not in robot.topEdge:
            self.location = self.location - 3
            self._logger.debug("Robot has moved right. At: {}".format(self.location))
            return True
        self._logger.debug("Robot can't move up")
        return False

    def moveDown(self):
        if self.location not in robot.botEdge:
            self.location = self.location + 3
            self._logger.debug("Robot has moved down. At: {}".format(self.location))
            return True
        self._logger.debug("Robot can't move down")
        return False

    def suck(self, env, murphy=False):
        sq = env[self.location]
        if not murphy:
            if sq.state == 'dirty':
                sq.clean()
                self._logger.debug("Square cleaned")
                return True
            else:
                self._logger.debug("Square already clean")
                return False
        else:
            murpNum = random.randint(0, 3)
            if murpNum == 2:
                sq.dirty()
            else:
                sq.clean()
            return True
        self._logger.debug("Square already clean")
        return False

    def doNothing(self):
        self._logger.debug("Robot does nothing")

    def checkEnv(self, env):
        sq = env[self.location]
        if sq.state == 'dirty':
            return True
        return False

    def murphyReflexAction(self, env):
        self.performanceMeasure = self.performanceMeasure + 1
        dirtSensorNum = random.randint(0, 9)
        isClean = self.checkEnv(env)
        if dirtSensorNum == 1:
        # dirt sensor went wrong
            isClean = not isClean

        if isClean:
            self.suck(env, True)
        else:
            self.moveAction()

    def moveAction(self):
        action = robot.actionMap[self.location]
        if action == 'left':
            self.moveLeft()
        elif action == 'right':
            self.moveRight()
        elif action == 'down':
            self.moveDown()
        elif action == 'start':
            self.location = 0

    def action(self, env):
        self.performanceMeasure = self.performanceMeasure + 1
        if self.checkEnv(env):
            self.suck(env)
        else:
            self.moveAction()

    def randomAction(self, env):
        self.performanceMeasure = self.performanceMeasure + 1
        action = robot.randomActionMap[random.randint(0, 5)]
        if action == 'up':
            self.moveUp()
        elif action == 'down':
            self.moveDown()
        elif action == 'left':
            self.moveLeft()
        elif action =='right':
            self.moveRight()
        elif action == 'suck':
            self.suck(env)
        elif action == 'nothing':
            self.doNothing()

    def murphyRandomAction(self, env):
        self.performanceMeasure = self.performanceMeasure + 1
        action = robot.randomActionMap[random.randint(0, 5)]
        if action == 'up':
            self.moveUp()
        elif action == 'down':
            self.moveDown()
        elif action == 'left':
            self.moveLeft()
        elif action =='right':
            self.moveRight()
        elif action == 'suck':
            dirtSensorNum = random.randint(0, 9)
            isClean = self.checkEnv(env)
            if dirtSensorNum == 1:
                isClean = not isClean
            if isClean:
                self.suck(env, True)
        elif action == 'nothing':
            self.doNothing()

def isWorldClean(env):
    for sq in env:
        if sq.state == 'dirty':
            return False
    return True

def runReflexAgent():
    for num in [1, 3, 5]:
        buf = list()
        for i in range(0, 99):
            world = vaccumWorld(num)
            robot1 = robot(0, True)
            while not isWorldClean(world.grid):
                robot1.action(world.grid)
            buf.append(robot1.performanceMeasure)
        print("Reflex Robot's performance: {a} in world with {b} dirt piles".format(a=mean(buf),
                b=num))

def runRandomAgent():
    for num in [1, 3, 5]:
        buf = list()
        for i in range(0, 99):
            world = vaccumWorld(num)
            robot1 = robot(0, True)
            while not isWorldClean(world.grid):
                robot1.randomAction(world.grid)
            buf.append(robot1.performanceMeasure)
        print("Random Robots performance: {a} in world with {b} dirt piles".format(a=mean(buf),
                b=num))

def runReflexMurphy():
    for num in [1, 3, 5]:
        buf = list()
        for i in range(0, 99):
            world = vaccumWorld(num)
            robot1 = robot(0, True)
            while not isWorldClean(world.grid):
                robot1.murphyReflexAction(world.grid)
            buf.append(robot1.performanceMeasure)
        print("Murphy Reflex Robots performance: {a} in world with {b} dirt piles".format(a=mean(buf),
                b=num))

def runRandomMurphy():
    for num in [1, 3, 5]:
        buf = list()
        for i in range(0, 99):
            world = vaccumWorld(num)
            robot1 = robot(0, True)
            while not isWorldClean(world.grid):
                robot1.murphyRandomAction(world.grid)
            buf.append(robot1.performanceMeasure)
        print("Murphy Random Robots performance: {a} in world with {b} dirt piles".format(a=mean(buf),
                b=num))


if __name__ == '__main__':
     runReflexAgent()
     runRandomAgent()
     runReflexMurphy()
     runRandomMurphy()
