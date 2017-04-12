# Tiger Game in Python
Tiger Game in Python 2.7 / 3.4+, based on the paper [Planning and acting in partially observable
stochastic domains](http://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf) by Leslie Kaelbling et al.

Requirements
--------------------------------------
Open a command prompt / terminal and execute : pip install joblib

Joblib is a multiprocessing library required by this game engine to execute
millions of runs in parallel on your machine.

Agent
--------------------------------------
Overwrite the code in agent.py (specificatlly the 'act' method).

Observations can be checked by self.observations and actions can be
taken using self.actions as shown in the example code (which uses
Leslie Kaelbling's optimal Finite State Machine model for the Tiger game).

To run the code, open a terminal / command line prompt at this location in the repository and use `python tigergame.py`.
To run with arguments use `python tigergame.py -v -load -t 1e5 -a 0.85 ...`

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