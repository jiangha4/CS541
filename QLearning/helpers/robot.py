import random

top_wall = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
left_wall = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
right_wall = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
bot_wall = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

class robot(object):
    actions = ['up', 'down', 'left', 'right', 'pickup']

    def __init__(self, learningRate, discounterFactor, qmatrix, steps):
        self.epsilon = .1
        self.discount_factor = discounterFactor
        self.learning_rate = learningRate
        self.qmatrix = qmatrix
        self.location = None
        self.steps = steps
        self.total_seen_rewards = 0

    def reset_total_rewards(self):
        self.total_seen_rewards = 0

    def set_location(self):
        self.location = random.randint(0, 99)

    def increase_epsilon(self):
        if not (self.epsilon == 1):
            self.epsilon = self.epsilon + 0.01

    def choose_action(self, state):
        if self.epsilon_greedy():
            # choose random action
            action = random.randint(0, 4)
        else:
            # choose best
            action = self.find_best_action(state)
        return action

    def perform_action(self, action, grid):
        reward = 0
        if robot.actions[action] == 'left':
            if self.location in left_wall:
                # hit wall
                reward = -5
            else:
                self.location -= 1
        elif robot.actions[action] == 'right':
            if self.location in right_wall:
                #hit wall
                reward = -5
            else:
                self.location += 1
        elif robot.actions[action] == 'up':
            if self.location in top_wall:
                reward = -5
            else:
                self.location -= 10
        elif robot.actions[action] == 'down':
            if self.location in bot_wall:
                reward = -5
            else:
                self.location += 10
        elif robot.actions[action] == 'pickup':
            if grid[self.location].contains_can:
                grid[self.location].cleaned()
                reward = 10
            else:
                reward = -1
        return reward

    def get_state(self, location, grid):
        curr = self.curr_sensor(location, grid)
        top = self.up_sensor(location-10, grid)
        bot = self.down_sensor(location+10, grid)
        left = self.left_sensor(location-1, grid)
        right = self.right_sensor(location+1, grid)

        return (curr, top, bot, left, right)

    def curr_sensor(self, location, grid):
        if grid[location].contains_can:
            return 1
        if grid[location].check_if_wall:
            return 2
        else:
            return 0

    def left_sensor(self, location, grid):
        if (location+1) in left_wall:
            return 2
        if grid[location].contains_can:
            return 1
        else:
            return 0

    def right_sensor(self, location, grid):
        if (location-1) in right_wall:
            return 2
        if grid[location].contains_can:
            return 1
        else:
            return 0

    def up_sensor(self, location, grid):
        if location in top_wall:
            return 2
        if location < 0:
            return 2
        if grid[location].contains_can:
            return 1
        else:
            return 0

    def down_sensor(self, location, grid):
        if location in bot_wall:
            return 2
        if location > 99:
            return 2
        if grid[location].contains_can:
            return 1
        else:
            return 0

    def find_best_action(self, state):
        buf = []
        for col in self.qmatrix:
            buf.append(col[state])
        return buf.index(max(buf))

    def find_q_max(self, state):
        buf = []
        for col in self.qmatrix:
            buf.append(col[state])
        return max(buf)

    def epsilon_greedy(self):
        rand = random.random()
        if rand <= self.epsilon:
            return True
        return False

    # Q-learning algorithm
    def run_episode(self, grid):
        cur_state = self.get_state(self.location, grid)
        action = self.choose_action(cur_state)
        cur_q_value = self.qmatrix[action][cur_state]
        reward = self.perform_action(action, grid)
        new_state = self.get_state(self.location, grid)
        q_max = self.find_q_max(new_state)
        new_q = cur_q_value + self.learning_rate*(reward + (self.discount_factor*q_max) - cur_q_value)
        self.qmatrix[action][cur_state] = new_q
        self.total_seen_rewards += reward

    def start(self, grid):
        for i in range(0, self.steps):
            self.run_episode(grid)


if __name__ == '__main__':
    pass
