import numpy as np
import gymnasium as gym
import pickle

#Environment for Gymnasium
env = gym.make('MountainCar-v0')

#Discretization for observation and action
positions_states = np.linspace(-1.2, 0.6, 18) #genera array di 18 valori equidistanti da -1.2 a 0.6
velocity_states = np.linspace(-0.07, 0.07, 28)

#Create an empty Q-table
def makeNewQTable():
    states = []
    for position in range(len(positions_states)+1):
        for velocity in range(len(velocity_states)+1):
            states.append((position, velocity))
    #print(states)        
    QTable = {}
    for state in states:
        for action in range(env.action_space.n):
            QTable[state, action] = 0
    #print(QTable)
    return QTable