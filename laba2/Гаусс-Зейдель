import numpy as np

from scipy.optimize import minimize_scalar
A=10
a=3
b=2

eps=1e-5
x_0=np.array([0,0])
k=1
j=1
y = np.copy(x_0)
n=2 
f = lambda x: A - (x[0]-a)*np.exp(-(x[0]-a)) - (x[1]-b)*np.exp(-(x[1]-b))
flag=True 
while flag:
    result = minimize_scalar(lambda lmbd: f(y + lmbd * np.eye(n)[j-1]))
    lmbd = result.x
     # Обновление y
    y = y + lmbd * np.eye(n)[j-1]

    if j < n:
        j += 1
    else:
        if np.linalg.norm(y - x_0) < eps:
            break
        else:
            x_0 = y
            j = 1
            k += 1

print(*y)
#3.9999999994850985 2.999999959169806
[4.         2.99999996]
