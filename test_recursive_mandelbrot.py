import shelve
from recursive_mandelbrot import display

db = shelve.open(r'C:\projekty\fractal\database', flag='r')
plot = db['arr']
db.close()

def test1():
    assert 1 in plot

def test2():
    assert None not in plot