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
A = HomeWork(1000,20,0.55)
A.Calculate()
print A.W
x = np.arange(len(A.W))
plt.plot(x,A.W,'bo-')
plt.show()

