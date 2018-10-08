import numpy as np
import random

class OneArmedBandit:
    
    def __init__(self):
        self.mean = 0
        self.values = []
        self.prob = np.random.random()
        
    def pull(self):
        temp = np.random.random()
        if (temp > self.prob):
            self.values.append(0)
            self.calcMean()
        else:
            self.values.append(10000)
            self.calcMean()
    
    def calcMean(self):
        temp = 0
        for value in self.values:
            temp += value
        self.mean = temp/len(self.values)
        
def experiment(b1, b2, b3, ep):
    p = np.random.random()
    bandits = [b1, b2, b3]
    if (p < ep):
        random.choice(bandits).pull()
    else:
        maximum = 0
        for bandit in bandits:
            maximum = max(bandit.mean, maximum)
        if b1.mean == maximum:
            b1.pull()
        elif b2.mean == maximum:
            b2.pull()
        else:
            b3.pull()

a = OneArmedBandit()
b = OneArmedBandit()
c = OneArmedBandit()
for i in range(10000):
    experiment(a, b, c, 0.05)
