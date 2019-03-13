from helpers.grid import *
from helpers.robot import *
from helpers.qmatrix import *

import argparse

def main(args):
    qmatrix = generate_qmatrix()
    robby = robot(learningRate=.2, discounterFactor=.9, qmatrix=qmatrix, steps=200)
    reward_plot = []
    # training
    for i in range(0, 5000):
        print("Training: Episode {}".format(i))
        # generate new grid every episode
        grid = make_grid()
        # set robby in new location
        robby.set_location()
        # run for 200 actions
        robby.start(grid)
        if i % 50 == 0:
            # increase epsilon every 50 epoches
            robby.increase_epsilon()
        if i % 100 == 0:
            # plot every 100 episodes
            reward_plot.append(robby.total_seen_rewards)
        # reset total seen rewards every episode
        robby.reset_total_rewards()

    # testing Robby
    robby.epsilon = .01
    robby.reset_total_rewards()
    test_rewards = []
    for i in range(0, 5000):
        print("Testing: Episode {}".format(i))
        grid = make_grid()
        robby.set_location()
        robby.start(grid)
        test_rewards.append(robby.total_seen_rewards)
        robby.reset_total_rewards()

    if args.graph:
        generate_training_graph(reward_plot)

    if args.numpy:
        generate_test_averages(test_rewards)


def generate_test_averages(rewards):
    import numpy as np

    std_dev = np.std(rewards)
    avg = sum(rewards)/5000

    print("Test Standard Deviation of rewards: {}".format(std_dev))
    print("Test Average over sum-of-rewards per episode: {}".format(avg))


def generate_training_graph(rewards):
    import matplotlib.pyplot as plt

    ep = [x for x in range(0, 5000) if x % 100 == 0]
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(ep, rewards)
    ax.set(xlabel='Episodes', ylabel='Total reward value per episode',
           title='Training Reward plot')
    plt.show()


def argument_parser():
    parser = argparse.ArgumentParser(description='PA3: Robby the Robot')
    parser.add_argument('-g', '--graph', action='store_true',
                        help='Show graphs. Must have matplotlib package installed')
    parser.add_argument('-n', '--numpy', action='store_true',
                        help='Calculate testing averages. Must have numpy package installed')
    return parser.parse_args()


if __name__ == '__main__':
    args = argument_parser()
    main(args)
