import numpy as np
from random import random
import math
import matplotlib.pyplot as plt

n = 10
N = 256
w = 900

def signal():
    signal = []
    for i in range(N):
        signal_point = 0
        for j in range(n):
            signal_point += random()*math.sin(w/n*((j+1)*i)+random())
        signal.append(signal_point)
    return signal

def Fp(signal):
    fp = []
    for p in range(N):
        fi = 0
        fr = 0
        for k in range(N):
            fi += signal[k]*math.sin((2*math.pi*p*k)/N)
            fr += signal[k]*math.cos((2*math.pi*p*k)/N)
        fp.append(math.sqrt(math.pow(fr, 2)+math.pow(fi,2)))
    return fp


def main():
    sig = signal()
    fp = Fp(sig)
    plt.plot(range(N),fp)
    plt.show()

main()