from matplotlib import pyplot as plt
from functions import *
from numpy import linspace as lin
import numpy as np

def heun_order2and3(f,t,u,h):
    k1 = f(t, u)
    k2 = f(t + h, u+h*k1)
    k3 = f(t+ 0.5*h, u+0.25*h*(k1+k2))

    return (h/6)*(k1+k2+4*k3)

def step_size_control(f):

    h=0.05
    a = 0.3
    u = [1]
    t = 0
    T = [t]
    tol = 1e-6
    while abs(t - a) > tol and t + h > t:
        if t + h > a:
            h = a - t
        e = abs(heun_order2and3(f,t,u[-1],h))
        if e > 1e-6:
            h = h/2
        elif e < 1e-7:
            h = 2*h
        else:
            t += h
            u_new = u[-1] + e
            u.append(u_new)
            T.append(t)
        print(t)

    return T, u

X,Y = step_size_control(ex_5_3f)
true_Y = apply_func_to_list(ex_5_3y, X)
plt.plot(X,true_Y, label='true')
plt.plot(X,np.array(Y), label='approx')
e = np.array(Y) - np.array(true_Y)
plt.plot(X,e, label='error')
plt.legend()
plt.show()




