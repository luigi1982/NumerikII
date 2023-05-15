from matplotlib import pyplot as plt
import numpy as np

from one_step_methods import *
from functions import *

t0 = 0
y0 = 1
phi = heun
N = 10
X,Y = apply_method(phi, t0, N, 1, y0, ex4_3f)
plt.plot(X,Y)
true_y = apply_func_to_list(ex4_3y, X)
plt.plot(X,true_y)
error = np.abs(np.array(true_y) - np.array(Y))
plt.plot(X,error)
if N==10:
    print(error)
else:
    print(error[::2])
plt.show()


