import numpy as np
from random import random
import math
import matplotlib.pyplot as plt

n = 10
N = 256
w = 900

new_coef = 0
existing_coef = 0

constant_coef = np.zeros((N,N,2))

def signal():
    signal = []
    for i in range(N):
        signal_point = 0
        for j in range(n):
            signal_point += random()*math.sin(w/n*((j+1)*i)+random())
        signal.append(signal_point)
    return signal

def Fp(signal):
    global new_coef
    global existing_coef
    fp = []
    for p in range(N):
        fi = 0
        fr = 0
        for k in range(N):
            if (constant_coef[p][k][0] == 0 and constant_coef[p][k][1] == 0):
                new_coef += 1
                constant_coef[p][k][0] = math.sin((2*math.pi*p*k)/N)
                constant_coef[p][k][1] = math.cos((2*math.pi*p*k)/N)
            else:
                existing_coef += 1
            fi += signal[k]*constant_coef[p][k][0]
            fr += signal[k]*constant_coef[p][k][1]
        fp.append(math.sqrt(math.pow(fr, 2)+math.pow(fi,2)))
    return fp

def main():
    sig = signal()
    fp = Fp(sig)
    f_test = Fp(sig)
    plt.plot(range(N),fp)
    print(" Added %d coefs, Used %d existed coef" %(new_coef, existing_coef))
    plt.show()

main()