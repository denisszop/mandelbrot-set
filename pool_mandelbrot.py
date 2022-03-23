import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

max_iter = 100
n = 200

def absv(a, b):
    x = x1 = a
    y = b
    for i in range(max_iter):
        if x ** 2 + y ** 2 >= 4:
            return i
        x = x ** 2 - y ** 2 + a
        y = 2 * x1 * y + b
        x1 = x
    return max_iter

def yarr(x):
    return [absv(x, y) for y in np.linspace(1, 0, n)]

if __name__ == '__main__':
    p = mp.Pool()
    plot = p.map(yarr, np.linspace(-2, 0.5, n))
    plot = np.asarray(plot)
    plot = np.delete(plot, (n - 1), axis=1)
    plot = np.concatenate((plot, np.flip(plot, axis=1)), axis=1)

    plt.imshow(plot.T, cmap='hot', extent = [-2, 0.5, -1, 1])
    plt.show()
