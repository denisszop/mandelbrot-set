import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import os
from functools import partial
import shelve
import time
#import imageio

folder = r'C:\Python\Projects\fractal'
start = time.time()

class display:
    def __init__(self, plot, x1, x2, y1):
        self.plot, self.x1, self.x2, self.y1 = plot, x1, x2, y1
    def render(self):
        plt.figure()
        plt.imshow(self.plot.T, cmap='hot', extent=[self.x1, self.x2, -1*self.y1, self.y1], aspect='auto')
        plt.xlabel('Real part')
        plt.ylabel('Imaginary part')
        plt.show()
        # odkomentowac, by stworzyc gif
        # filename = f'{y1}.jpg'
        # filenames.append(filename)
        # plt.savefig(folder + filename)
        # plt.close()
        global max_iter 
        max_iter -= 5

#n zmienia rozdzielczosc, przy wiekszym przyblizeniu liczba iteracji musi byc znacznie wieksza
max_iter = 100
n = 200
#tworzy liste zakresow x, zmienic ostatnia wartosc (musi byc podzielna przez dwa), by utworzyc kolejne przyblizenia wykresu
zoomx = np.linspace(-2, 0.5, 2)
#filenames = []

#zbior mandelbrota: f_c(z) = z ** 2 + c, seed = 0, c = stała liczba zespolona
#(0 + 0i)(0 + 0i) + (0.5 + 0.5i) = (0.5 + 0.5i)
#(0.5 + 0.5i)(0.5 + 0.5i) + (0.5 + 0.5i) = ...
#x ** 2 + y ** 2 >= 4; jeeli wartość absolutna sumy x i y jest wieksza niz 2, funkcja jest rozbiezna do nieskonczonosci
#kolejna iteracja, z ** 2 = (a = x ** 2 - y ** 2, b = 2 * x * y) + c

def absv(a, b, x, y, i):
    if x ** 2 + y ** 2 >= 4 or i == max_iter:
        return i
    if i < max_iter:
        return absv(a, b, x ** 2 - y ** 2 + a, 2 * x * y + b, i + 1)
def yarr(y1, x):
    return [absv(x, y, x, y, 0) for y in np.linspace(y1, 0, n)]

if __name__ == '__main__':
    cores = mp.cpu_count()
    #bierze pierwsza i ostatnia pozycje z listy zoomx, by ustalic zakres x i y
    while zoomx.size >= 2:
        if zoomx.size == 2:
            x1, x2 = 0, 1
        else:
            x1, x2 = zoomx.size // 2 - 1, zoomx.size // 2
        #zakres y = stosunek pomniejszonego do oryginalnego zakresu x
        y1 = zoomx[x1] / (-2)

        #tworzy nowe procesy i dzieli obliczanie wartosci dla wykresu miedzy nimi i przypisuje je do numpy array
        with mp.Pool(processes=cores) as p:
            plot = p.map(partial(yarr, y1), np.linspace(zoomx[x1], zoomx[x2], n))
            plot = np.asarray(plot)
            #zbior mandelbrota jest symetryczny wokol osi x, wiec liczy jedynie gorna polowe, kopiuje, obraca wokol osi x i przylacza do wykresu
            plot = np.delete(plot, (n - 1), axis=1)
            plot = np.concatenate((plot, np.flip(plot, axis=1)), axis=1)

            db = shelve.open(folder + r'\database\db', flag='n')
            db['arr'] = plot
            db.close()

            print(time.time() - start)
            img = display(plot, zoomx[x1], zoomx[x2], y1)
            img.render()

            zoomx = np.delete(zoomx, [x1, x2])
    # odkomentowac, by stworzyc gif
    # with imageio.get_writer(folder + 'gif1.gif', mode='I') as writer:
    #     for filename in filenames:
    #         image = imageio.v3.imread(folder + filename)
    #         writer.append_data(image)
    #         os.remove(folder + filename)
