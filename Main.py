__author__ = 'TriNguyenDang'

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

class HomeWork(object):
    T = None
    W = None
    p = None
    def __init__(self,TMax,W0,p):
        self.T = TMax
        self.W = [W0]
        self.p = p
        t = 1
        while(t <= self.T):
            if(self.W[t - 1] > 0):
                tmp = 2 * bernoulli.rvs(self.p) - 1 + self.W[t-1]
                if(tmp >= 0):
                    self.W.append(tmp)
                else:
                    self.W.append(0)
            else:
                self.W.append(0)
            t+=1
    def Calculate(self):
        t = 1
        while(t <= self.T):
            if(self.W[t - 1] > 0):
                tmp = 2 * bernoulli.rvs(self.p) - 1 + self.W[t-1]
                if(tmp >= 0):
                    self.W.append(tmp)
                else:
                    self.W.append(0)
            else:
                self.W.append(0)
            t+=1
    def Draw(self,Color,Marker):
        x = np.arange(len(self.W))
        plt.plot(x,self.W,color = Color, marker = Marker, label = 'p='+str(self.p))
A = HomeWork(1000,20,0.55)
B = HomeWork(1000,20,0.25)
C = HomeWork(1000,20,0.50)

A.Draw('red','o')
B.Draw('blue','1')
C.Draw('green','*')


plt.grid(True)
plt.legend(loc = 0)
plt.show()

