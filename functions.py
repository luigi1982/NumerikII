def apply_func_to_list(f,l):
    y = []
    for x in l:
        y.append(f(x))
    return y

def ex4_3f(t,z):
    return -2*t*z**2

def ex4_3y(t):
    return 1/(t**2 + 1)

def ex_5_3f(t,z):
    return -2*t*z**2

def ex_5_3y(t):
    return 1/(t**2+1)