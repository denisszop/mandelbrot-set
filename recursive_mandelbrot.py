import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

max_iter = 100
n = 200

def absv(a, b, x, y, i):
    if x ** 2 + y ** 2 >= 4 or i == max_iter:
        return i
    if i < max_iter:
        return absv(a, b, x ** 2 - y ** 2 + a, 2 * x * y + b, i + 1)
def yarr(x):
    return [absv(x, y, x, y, 0) for y in np.linspace(1, 0, n)]

if __name__ == '__main__':
    #for x, y in (np.linspace(x), np.linspace(y)): -> zoom
    p = mp.Pool()
    plot = p.map(yarr, np.linspace(-2, 0.5, n))

    plot = np.asarray(plot)
    plot = np.delete(plot, (n - 1), axis=1)
    plot = np.concatenate((plot, np.flip(plot, axis=1)), axis=1)

    plt.imshow(plot.T, cmap='hot', extent = [-2, 0.5, -1, 1])
    plt.show()