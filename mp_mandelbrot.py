import numpy
from multiprocessing import Process, Array
import ctypes
import matplotlib.pyplot as p
import time
import shelve

start_time = time.time()
max_iter = 100
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

def f(a, y1, y2, yindex):
    arr = numpy.frombuffer(a.get_obj()) # mp_arr and arr share the same memory
    arr = arr.reshape((w, h)) # b and arr share the same memory
    
    for iy, i in enumerate(numpy.linspace(y1, y2, int(n / 4)), start=yindex):
        for jx, j in enumerate(numpy.linspace(-2, 0.5, n)):
            arr[jx, iy] = absv(j, i)

w = h = n = 1000 #must be even

if __name__ == '__main__':
    mp_plot = Array(ctypes.c_double, w*h)
    arr = numpy.frombuffer(mp_plot.get_obj())
    arr = arr.reshape((w, h))

    p1 = Process(target=f, args=(mp_plot, 1, 0.75, 0))
    p1.start()
    p2 = Process(target=f, args=(mp_plot, 0.75, 0.5, int(h / 4)))
    p2.start()
    p3 = Process(target=f, args=(mp_plot, 0.5, 0.25, int(h / 2)))
    p3.start()
    p4 = Process(target=f, args=(mp_plot, 0.25, 0, int(h * 0.75)))
    p4.start()
    proc = [p1, p2, p3, p4]
    for pr in proc:
        pr.join()

    arr = numpy.delete(arr, (n - 1), axis=1)
    arr = numpy.concatenate((arr, numpy.flip(arr, axis=1)), axis=1)

    db = shelve.open(r'D:\fractal\numpyarr', flag='n')
    db['arr'] = arr
    db.close()
    
    print(time.time() - start_time)
    p.figure(dpi=100)
    p.imshow(arr.T, cmap='hot', extent=[-2, 1, -1, 1])
    p.xlabel('Real part')
    p.ylabel('Imaginary part')
    p.show()
# import numpy
# print(numpy.linspace(0, 0 + (0.5 * 4), 4, endpoint=False))