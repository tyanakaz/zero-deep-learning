import numpy as np
import matplotlib.pyplot as plt
import sys

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
args = sys.argv
max_num = int(args[1])

x = np.arange(1, 11) 
vsigmoid = np.vectorize(sigmoid)
vsigmoid(x)

y = vsigmoid(x)
plt.plot(x,y)

