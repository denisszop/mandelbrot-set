import time
import numpy
import matplotlib.pyplot as p
import shelve

#mandelbrot set: f_c(z) = z ** 2 + c, seed = 0, c = point in plot of complex numbers
#check if x ** 2 + y ** 2 >= 4
#if not, z ** 2 = (x ** 2 - y ** 2, 2 * x * y)
#add c

start_time = time.time()
max_iter = 100

def f(a, b):
    x = x1 = a
    y = b
    for i in range(max_iter):
        if x ** 2 + y ** 2 >= 4:
            return i
        x = x ** 2 - y ** 2 + a
        y = 2 * x1 * y + b
        x1 = x

    return max_iter


#defines a 2d plot[x, y]
n = 10000
w = h = n
plot = numpy.zeros([w, h])

#assigns a color value for each point on the complex plane that diverges to infinity
x = y = 0
for i in numpy.linspace(2, -2, n):
    for j in numpy.linspace(-2, 2, n):
        c = f(j, i)
        plot[x, y] = c
        x += 1
    x = 0
    y += 1
    print(time.time() - start_time)

db = shelve.open(r'C:\fractal\numpyarr', flag='n')
db['arr'] = plot
db.close()

p.figure(dpi=100)
p.imshow(plot.T, cmap='hot', extent=[-2, 1, -1, 1])
p.xlabel('Real part')
p.ylabel('Imaginary part')
p.show()