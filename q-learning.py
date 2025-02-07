#from functionHelper import getState, cresteEmptyQTable, maxAction, save_obj
import gymnasium as gym
import random
import numpy as np

#Initializing the Gymnasium's environment
#import gymnasium as gym
#env = gym.make("MountainCar-v0", render_mode="rgb_array", goal_velocity=0.1)  # default goal_velocity=0
#env<TimeLimit<OrderEnforcing<PassiveEnvChecker<MountainCarEnv<MountainCar-v0>>>>>
#env.reset(seed=123, options={"x_init": np.pi/2, "y_init": 0.5})  # default x_init=np.pi, y_init=1.0
#(array([-0.46352962,  0.        ], dtype=float32), {})

env = gym.make('MountainCar-v0', max_episode_step = 1000)

#Hyperparameters
learning_rate = 0.1 #alpha
discount_factor = 0.9 #gamma
initial_epsilon = 1.0 #Start value of epsilon/ e-Greedy
min_epsilon = 0.01 #Min value of epsilon
episodes = 5000 #Max number of episodes

#Empty Q-table
q_table = createEmptyQTable()