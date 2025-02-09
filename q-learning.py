from functionHelper import makeNewQTable, bestAction
import gymnasium as gym
import random
import numpy as np

#Initializing the Gymnasium's environment
env = gym.make('MountainCar-v0') #crea una instanza dell'ambiente di Mountain Car
env._max_episodes_step = 1000 #imposta il numero di azioni che l'agente può fare
                               #in un singolo episodio
#Hyperparameters
learningRate = 0.1 #alpha
discountFactor = 0.9 #gamma
initialEpsilon = 1.0 #Start value of epsilon/ e-Greedy
minEpsilon = 0.01 #Min value of epsilon
episodes = 5000 #Max number of episodes
epsilonDec = 2 / episodes

#Empty Q-table
q_table = makeNewQTable()
print("Creo la Q-table")

#To keep trackof the total score at each episode
total_score = np.zeros(episodes) #Creo un array di lunghezza episodes con tutti 0

def choose_action(state, epsilon):
    #Choose an action using the e-greedy strategy
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample() #sceglie casualmente un azione tra quelle disponibili
    else:
        return bestAction(q_table, state)
print ("Arrivo anche qui")

def newQValue():
    return

#Training the agent with all the episodes
def trainingAgent():
    for episode in range(episodes):
        return
