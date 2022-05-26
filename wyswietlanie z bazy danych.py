import shelve
import matplotlib.pyplot as plt
from recursive_mandelbrot import display

db = shelve.open(r'C:\projekty\fractal\database', flag='r')
plot = db['arr']
db.close()

plot = display(plot)
plot.render()