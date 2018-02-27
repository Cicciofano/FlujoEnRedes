from random import random
from math import ceil, sqrt


def distancia(p,q):
    return sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))

class Grafo:

    def __init__(self, orden=30, prob = 1, radio = 0.45):
        self.n = orden
        self.m = ceil(orden/5)
        self.p = prob
        self.r = radio
        self.nodos = []
        self.aristas = []

    def CreaNodos(self):
        for t in range(self.n):
            x=random()
            y=random()
            self.nodos.append((x,y))

    def CreaAristas(self):
        with open ("nodos.dat", "w") as crear:
            t=0
            for(x2,y2) in self.nodos[0:self.n+1]:
                print(x2,y2,t,file=crear)
            t=1
            for(x1,y1) in self.nodos[0:self.m]:
                print(x1,y1,t, file=crear)
                t =t+1
            t=1
            for(x1,y1) in self.nodos[0:self.m]:
                for(x2,y2) in self.nodos[self.m:self.n]:
                    if distancia((x1,y1),(x2,y2))<self.r:
                        self.aristas.append((x1,y1,x2,y2))
                        print(x2,y2,t, file=crear)
                t=t+1

    def ArchivoGnu(self):
        with open("tarea2.plot","w") as archivo:
            print("set term png", file=archivo)
            print("set output 'graficat2.png'", file=archivo)
            print("set xrange [0:1]", file=archivo)
            print("set yrange [0:1]", file=archivo)
            print("set pointsize 3", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=1
            for a in self.aristas:
                (x1,y1,x2,y2)=a
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num,x1,y1,x2,y2),file=archivo)
                num+=1
            print("show arrow", file=archivo)
            print("plot 'nodos.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
            print("quit()",file=archivo)
        
        
           
G=Grafo()
G.CreaNodos()
G.CreaAristas()
G.CreaAristas()
G.ArchivoGnu()
