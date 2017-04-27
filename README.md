# Tiger Game in Python
Tiger Game in Python 2.7 / 3.4+, based on the paper [Planning and acting in partially observable
stochastic domains](http://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf) by Leslie Kaelbling et al.

Requirements
--------------------------------------
Open a command prompt / terminal and execute : `pip install joblib numpy`

Joblib is a multiprocessing library required by this game engine to serialize and deserialize the models.

Numpy is the standard numeric library to handle large matrix manipulations, and is
required for solving the problem using Evolution Strategies (ES).

Agent
--------------------------------------
Overwrite the code in agent.py (specificatlly the 'act' method).

Observations can be checked by self.observations and actions can be
taken using self.actions as shown in the example code (which uses
Leslie Kaelbling's optimal Finite State Machine model for the Tiger game).

To run the code, open a terminal / command line prompt at this location in the repository and use `python tigergame.py`.
To run with arguments use `python tigergame.py -v -load -t 1e5 -a 0.85 ...`

Note : The act() method in the agent has the observation, score and a mode parameter called `learn`.

This `learn` parameter is to decide between training and testing time execution of the agent. If true, it means
the agent must be trained, else it must only act without training the model further.

Parameters
--------------------------------------

There are various parameters which can be modified to alter the game behaviour,
however it is recommended to keep all parameters unchanged to conform to the original paper.

-i    :   Number of iterations  (default 10000) <br>
-t    :   Number of timesteps   (default 100)   <br>
-r    :   Default reward value  (default 10.0)  <br>
-a    :   Listening accuracy    (default 0.85)  <br>
-tp   :   Tiger penalty valye   (default -100)  <br>
-lp   :   Listening penalty     (default -1)  <br>
-seed :   Random seed value     (default -1, which means no random seed)  <br>
-v    :   Verbosity of the game (there is no default, add -v during execution to enable print statements) <br>
-load :   Load agent from file instead of creating new. (default is false, to enable just pass -load)

Performance
-----------

100 million games with default settings - 4 minutes 16 seconds
