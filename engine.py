from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import random
from joblib import Parallel, delayed

class ConstError(TypeError): pass


ACTION_NAMES = {0 : "Listen",
                1 : "Open Left",
                -1: "Open Right"}


OBSERVATION_NAMES = {0 : "No Observation",
                     1 : "Growl Left",
                     -1: "Growl Right"}

class Action(object):
    def __init__(self):
        self.ACTION_OPEN_LEFT = 1
        self.ACTION_OPEN_RIGHT = -1
        self.ACTION_LISTEN = 0

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ConstError('Cannot modify action : %s' % key)

        self.__dict__[key] = value


class Observations(object):
    def __init__(self):
        self.NO_OBSERVATION = 0
        self.GROWL_LEFT = 1
        self.GROWL_RIGHT = -1

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ConstError('Cannot modify Observation : %s' % key)

        self.__dict__[key] = value


class Game(object):

    def __init__(self, agent, listening_accuracy=0.85, reward=10.,
                 listening_penaly=-1., tiger_penalty=-100., random_seed=None, verbose=False) :

        self.agent = agent
        self.listening_acc = listening_accuracy
        self.reward = reward
        self.listening_penalty = listening_penaly
        self.tiger_penalty = tiger_penalty

        self.actions = Action()
        self.observations = Observations()

        random.seed(random_seed)
        self.verbose = verbose


    def play_rounds(self, nb_rounds=100):
        nb_rounds = int(nb_rounds)
        print("Playing Tiger game %d times" % (nb_rounds))

        scores = Parallel(n_jobs=-2, verbose=1)(delayed(self._play_game)(i) for i in range(nb_rounds))

        print('*' * 80)
        print()
        print("Total score : ", sum(scores))
        print("Average score : ", sum(scores) / len(scores))

    def _play_game(self, i):
        if self.verbose: print("Beginning game : %d" % (i + 1))
        if self.verbose: print('*' * 80)

        self.__initialize_state()  # initialize the game

        if self.verbose: print("Observed : ", OBSERVATION_NAMES[0])

        action = self.agent.act(self.observations.NO_OBSERVATION)  # initial action (unbiased observation)
        self.score += self.__reward(action)

        if self.verbose: print("Performed action :", ACTION_NAMES[action])
        if self.verbose: print()

        while not self.__check_open_wrong_door(action):
            if action in [self.actions.ACTION_OPEN_LEFT, self.actions.ACTION_OPEN_RIGHT]:
                self.__update_state(action)  # randomly update tiger location
                observation = self.observations.NO_OBSERVATION  # no observation at this time
            else:
                observation = self.__observe()

            if self.verbose: print("Observed : ", OBSERVATION_NAMES[observation])

            action = self.agent.act(observation)

            if self.verbose: print("Performed action :", ACTION_NAMES[action])
            if self.verbose: print()

            self.score += self.__reward(action)

        # game ending
        self.score += self.tiger_penalty
        if self.verbose: print("Game %d : " % (i + 1))
        if self.verbose: print(self)  # print game
        if self.verbose: print()

        return self.score

    def __initialize_state(self):
        self.__tiger_loc = 0 if random.random() < 0.5 else 1 # 0 indicates TL, 1 indicates TR
        self.score = 0.0


    def __update_state(self, action):
        if action in [self.actions.ACTION_OPEN_LEFT, self.actions.ACTION_OPEN_RIGHT]:
            self.__tiger_loc = 0 if random.random() < 0.5 else 1  # 0 indicates TL, 1 indicates TR


    def __reward(self, action):
        if action in [self.actions.ACTION_OPEN_LEFT, self.actions.ACTION_OPEN_RIGHT]:
            if self.__check_open_wrong_door(action):
                return self.tiger_penalty # Opened wrong door, get penalty
            else:
                return self.reward # Get the gold value
        else:
            return self.listening_acc # Get listening penalty


    def __check_open_wrong_door(self, action):
        if self.__tiger_loc == 0 and action == self.actions.ACTION_OPEN_LEFT:
            return True
        elif self.__tiger_loc == 1 and action == self.actions.ACTION_OPEN_RIGHT:
            return True
        else:
            return False


    def __observe(self):
        prob = random.random()

        if prob <= self.listening_acc:
            if self.__tiger_loc == 0:
                return self.observations.GROWL_LEFT
            else:
                return self.observations.GROWL_RIGHT
        else:
            if self.__tiger_loc == 0:
                return self.observations.GROWL_RIGHT
            else:
                return self.observations.GROWL_LEFT


    def __str__(self):
        out = "Score : %0.2f" % (self.score)
        return out