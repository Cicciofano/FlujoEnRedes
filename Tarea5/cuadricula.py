from random import random
from math import ceil, floor, sqrt

def distancia(p,q):
    return 
def pmedio(p,q):
    return ((p[0]+q[0])/2),((p[1]+q[1])/2)

class Grafo:  
    def __init__(self, prob = 1, radio = 4.5):
        self.k = k
        #self.m = ceil(Nnodos/5)
        self.p = prob
        self.r = radio
        self.nodos = []
        self.aristas = []
        self.pm = []
        self.pesos = []
        self.colores = []
        
    def CreaNodos(self,k):
        with open ("nodos.dat", "w") as crear:
            for t in range(1,k+1):
                for tt in range(1,k+1):
                    x=tt
                    y=t
                    self.nodos.append((x,y))
                    print(x,y, file=crear)
            
    def CreaAristas(self):
        with open ("aristas.dat", "w") as crear:






























            
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
                        self.pm.append(pmedio((x1,y1),(x2,y2)))
                        self.aristas.append((x1,y1,x2,y2))
                        self.pesos.append(ceil(distancia((x1,y1),(x2,y2))))
                        self.colores.append(t)
                        print(x2,y2,t, file=crear)
                t=t+1

    def ArchivoGnu(self):
        with open("tarea4.plot","w") as archivo:
            print("set term pdf", file=archivo)
            print("set output 'tarea4.pdf'", file=archivo)
            print("set xrange [0: {:d}]".format(k+1), file=archivo)
            print("set yrange [0: {:d}]".format(k+1), file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
##            num=1
##            for a in range (len(self.aristas)):
##                (x1,y1,x2,y2) = self.aristas[a]
##                (xm,ym) = self.pm[a]
##                w = self.pesos[a]
##                col = self.colores[a]
##                if dirigido is 1:
##                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size .5,10 lt {:f} lw 1".format(num,x1,y1,x2,y2,col),file=archivo)
##                    if pesos is 1:
##                        print("set label font ',9' '{:d}' at {:f}, {:f} tc lt {:f}".format(w, xm, ym, col), file = archivo)                        
##                else:
##                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:f} lw 1".format(num,x1,y1,x2,y2,col),file=archivo)
##                    if pesos is 1:
##                        print("set label font ',9' '{:d}' at {:f}, {:f} tc lt {:f}".format(w, xm, ym, col), file = archivo)                    
##                num+=1            
            print("plot 'nodos.dat' using 1:2 with points pt 5", file=archivo)
##            print("show arrow", file=archivo)
            print("quit()",file=archivo)

k = 7
dirigido = 1 # no dirigido = 0 / dirigido = 1
pesos = 1    # sin pesos   = 0 / con pesos =1
G=Grafo()
G.CreaNodos(k)
#G.CreaAristas()
G.ArchivoGnu()

#0-gris
#1-morado
#2-verde
#3-celeste
#4-naranja
#5-amarillo
#6-azul
#7-rojo
#8-negro
