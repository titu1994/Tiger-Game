from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import numpy as np
import joblib
import os

from consts import *

AGENT_NAME = "Smith"


def serialize_agent(agent):
    joblib.dump(agent, filename='agent.pkl')
    print('Agent saved')


def deserialize_agent():
    if os.path.exists('agent.pkl'):
        agent = joblib.load('agent.pkl')
    else:
        print("Agent data does not exist. Creating default agent.")
        agent = Agent()

    return agent


class Agent(object):

    def __init__(self):
        self.name = AGENT_NAME
        self.actions = Action()
        self.observations = Observations()

        self.left_listen_count = 0
        self.right_listen_count = 0

    def act(self, observation, score, learn):
        # Example of Leslie Kaelbling's optimal agent model,
        # minus the bottom part of the Finite State Machine

        if observation == self.observations.NO_OBSERVATION:
            # reset belief state
            self.left_listen_count = 0
            self.right_listen_count = 0

            # begin by listening
            return self.actions.ACTION_LISTEN
        else:
            # update internal count
            if observation == self.observations.GROWL_LEFT:
                self.left_listen_count += 1
            else:
                self.right_listen_count += 1

            # perform action
            if self.left_listen_count == 2:
                # reset listen count since we made an informed decision
                self.left_listen_count = 0
                return self.actions.ACTION_OPEN_RIGHT

            elif self.right_listen_count == 2:
                # reset listen count since we made an informed decision
                self.right_listen_count = 0
                return self.actions.ACTION_OPEN_LEFT

            elif self.left_listen_count >= 1 and self.right_listen_count >= 1:
                # we obtained dis-confirming growls. Reset our belief state
                self.left_listen_count = 0
                self.right_listen_count = 0

                return self.actions.ACTION_LISTEN
            else:
                # not enough information to make informed decision
                # simply listen
                return self.actions.ACTION_LISTEN

    def __str__(self):
        return "Agent %s" % (self.name)