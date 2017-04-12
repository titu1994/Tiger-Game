from __future__ import print_function
from __future__ import absolute_import
from __future__ import division


class ConstError(TypeError): pass

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
