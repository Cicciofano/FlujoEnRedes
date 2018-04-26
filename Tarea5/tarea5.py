from random import random
from math import ceil, floor, sqrt

def distancia(p,q):
    return (abs(q[0]-p[0])+ abs(q[1]-p[1]))
def pmedio(p,q):
    return ((p[0]+q[0])/2),((p[1]+q[1])/2)

class Grafo:  
    def __init__(self, prob = 1, radio = 4.5):
        self.k = k
        self.p = prob
        self.r = radio
        self.nodos = dict()
        self.aristas = dict()
        self.pesos = []
        self.colores = []
        
    def CreaNodos(self,k):
        with open ("cuadricula.dat", "w") as crear:
            n=0
            for t in range(1,k+1):
                for tt in range(1,k+1):
                    x=tt
                    y=t
                    self.nodos[n+1] = (tt,t)
                    print(tt,t, file=crear)
                    n=n+1

            
    def CreaAristas(self,l):
        with open ("nodos.dat", "w") as crear:
            for n in (self.nodos):
                for nn in (self.nodos):
                    if n is not nn:
                        if distancia (self.nodos[n], self.nodos[nn]) < l+1:
                            self.aristas[G.nodos[n],G.nodos[nn]] = self.aristas[G.nodos[nn],G.nodos[n]] = l
            print(self.aristas, file=crear)

##            t=0
##            for(x2,y2) in self.nodos[0:self.n+1]:
##                print(x2,y2,t,file=crear)
##            t=1
##            for(x1,y1) in self.nodos[0:self.m]:
##                print(x1,y1,t, file=crear)
##                t =t+1
##            t=1
##            for(x1,y1) in self.nodos[0:self.m]:
##                for(x2,y2) in self.nodos[self.m:self.n]:
##                    if distancia((x1,y1),(x2,y2))<self.r:
##                        self.pm.append(pmedio((x1,y1),(x2,y2)))
##                        self.aristas.append((x1,y1,x2,y2))
##                        self.pesos.append(ceil(distancia((x1,y1),(x2,y2))))
##                        self.colores.append(t)
##                        print(x2,y2,t, file=crear)
##                t=t+1

    def ArchivoGnu(self):
        with open("tarea5.plot","w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'tarea5.eps'", file=archivo)
            print("set xrange [0: {:d}]".format(k+1), file=archivo)
            print("set yrange [0: {:d}]".format(k+1), file=archivo)
            print("set pointsize .5", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)      
            num=1
            for a in self.aristas:
                p1=a[0]
                p2=a[1]
                x1=p1[0]
                y1=p1[1]
                x2=p2[0]
                y2=p2[1]
                print("set arrow {:d} from {:d}, {:d} to {:d}, {:d} nohead".format(num,x1,y1,x2,y2),file=archivo)
                num+=1      
            print("show arrow", file=archivo)
            print("plot 'cuadricula.dat' using 1:2 with points pt 5", file=archivo)
            print("quit()",file=archivo)

k = 6
l = 2
G=Grafo()
G.CreaNodos(k)
G.CreaAristas(l)
G.ArchivoGnu()
