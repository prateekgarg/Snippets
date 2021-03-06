#/bin/python

from scipy import *
from matplotlib.pyplot import *

x0 = 1
a = 0.125
b = 0.5
k = 0.75
B = 1
C = 1
T = 1

niters = 50
numerical_iters = 100
xval = zeros(niters)
#xval[:T] = 1

for T in [1]:
    xval[0] = x0
    for i in range(T, niters):
        x_old = 1
        x_new = 1
        for j in range(numerical_iters):
            x_new = xval[i-1] + (1.0/T) * xval[i-T]*(a * pow(T*x_old, k-1) -
                                        b * T * x_old*pow(T*xval[i-T]/C, B))
            x_old = x_new
        xval[i] = x_new
    l = 'T = ' + str(T)
    myplot = plot(range(niters), xval, label = l)
    #phase_plot = plot(xval[:-1], xval[:-1]-xval[1:], label = l)
legend(loc='upper right')
show()
