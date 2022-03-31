import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time

max_iter = 100
n = 4
z = 2

def absv(a, b, x, y, i):
    if x ** 2 + y ** 2 >= 4 or i == max_iter:
        return i
    else:
        return absv(a, b, x ** 2 - y ** 2 + a, 2 * x * y + b, i + 1)
    

def yarr(x):
    return x

if __name__ == '__main__':
    for y1, y2 in zip(np.linspace(1, 0.4, z), np.linspace(0, 0.3, z)):
        for x1, x2 in zip(np.linspace(-2, -1, z), np.linspace(0.5, 0, z)):
            p = mp.Pool()
            start_time = time.time()
            plot = p.map(yarr, [np.linspace(x1, x2, n), y1, y2])

            print(plot[0])
# for x, y in zip(np.linspace(-2, -1, 4), np.linspace(0.5, 0, 4)):
#     print(x, y)
