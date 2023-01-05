from scipy.optimize import *
from math import cos 

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

# print(myroot)


# Minimizing a function
def eqn2(x):
    return x**2 + x + 2

mymin = minimize(eqn2, 0, method="BFGS")

print(mymin)