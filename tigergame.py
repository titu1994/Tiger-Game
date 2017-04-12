from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import argparse
import time

from agent import Agent
from engine import Game

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tiger Game argument parser')

    parser.add_argument('-t', default=10000, type=int, help='Number of iterations')
    parser.add_argument('-r', default=10., type=float, help='Gold reward value')
    parser.add_argument('-a', default=0.85, type=float, help='Listening accuracy')
    parser.add_argument('-tp', default=-100.0, type=float, help='Tiger penalty value')
    parser.add_argument('-lp', default=-1.0, type=float, help='Listening penalty')

    parser.add_argument('-seed', default=-1, type=int, help='Random seed. Set to -1 to remove seed.')
    parser.add_argument('-v', dest='verbose', action='store_true', help='Print working of code')

    parser.set_defaults(verbose=False)
    args = parser.parse_args()

    nb_iterations = args.t
    reward_val = args.r
    listening_acc = args.a
    tiger_penalty = args.tp
    listening_penalty = args.lp

    seed = args.seed
    if seed == -1:
        seed = None
    verbose = args.verbose

    game = Game(listening_acc, reward_val, listening_penalty,
                tiger_penalty, seed, verbose)

    t1 = time.time()
    game.play_rounds(nb_rounds=nb_iterations)
    t2 = time.time()

    print()
    print("Played %d games in time : %0.4f seconds" % (nb_iterations, t2 - t1))