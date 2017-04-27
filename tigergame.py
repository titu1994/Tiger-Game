from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import argparse
import time

from agent import Agent, serialize_agent, deserialize_agent
from engine import Game

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tiger Game argument parser')

    parser.add_argument('-i', default=10000, type=int, help='Number of iterations')
    parser.add_argument('-t', default=100, type=int, help='Number of time steps per game')
    parser.add_argument('-r', default=10., type=float, help='Gold reward value')
    parser.add_argument('-a', default=0.85, type=float, help='Listening accuracy')
    parser.add_argument('-tp', default=-100.0, type=float, help='Tiger penalty value')
    parser.add_argument('-lp', default=-1.0, type=float, help='Listening penalty')

    parser.add_argument('-seed', default=-1, type=int, help='Random seed. Set to -1 to remove seed.')
    parser.add_argument('-v', dest='verbose', action='store_true', help='Print working of code')
    parser.add_argument('-load', dest='load', action='store_false', help='Load the agent from file')

    parser.set_defaults(verbose=False, load=False)
    args = parser.parse_args()

    nb_iterations = args.i
    nb_timesteps = args.t
    reward_val = args.r
    listening_acc = args.a
    tiger_penalty = args.tp
    listening_penalty = args.lp

    seed = args.seed
    if seed == -1:
        seed = None
    verbose = args.verbose
    load_agent = args.load

    if load_agent:
        agent = deserialize_agent()
    else:
        agent = Agent()

    learn = True if not load_agent else False

    game = Game(agent, listening_acc, reward_val, nb_timesteps,
                listening_penalty, tiger_penalty, seed, verbose, learn)

    t1 = time.time()
    game.play_rounds(nb_rounds=nb_iterations)
    t2 = time.time()

    print()
    print("Played %d games in time : %0.4f seconds" % (nb_iterations, t2 - t1))

    if not load_agent and os.path.exists('agent.pkl'):
        ch = input("Agent data already exists. Overwrite ? y/n : ")

        if ch == 'y':
            print('Overwriting previous agent')
            serialize_agent(agent)
    else:
        serialize_agent(agent)