from random import random
from math import ceil, floor, sqrt

def distancia(p,q):
    return sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))
def pmedio(p,q):
    return ((p[0]+q[0])/2),((p[1]+q[1])/2)

class Grafo:
    def __init__(self, prob = 1, radio = 3):
        self.n = Nnodos
        self.m = ceil(Nnodos/5)
        self.p = prob
        self.r = radio
        self.nodos = []
        self.vecinos = dict()
        self.arcos = dict()
        
    def CreaNodos(self):
        for t in range(self.n):
            x=10*random()
            y=10*random()
            self.nodos.append((x,y))
            if not (x,y) in self.vecinos:
                self.vecinos[(x,y)] = set()
            
    def CreaAristas(self):
        for(x1,y1) in self.nodos[0:self.m]:
            for(x2,y2) in self.nodos[self.m:self.n]:
                if distancia((x1,y1),(x2,y2))<self.r:
                    self.arcos[(x1,y1),(x2,y2)] = ceil(distancia((x1,y1),(x2,y2)))
                    self.arcos[(x2,y2),(x1,y1)] = ceil(distancia((x1,y1),(x2,y2)))
                    self.vecinos[(x1,y1)].add((x2,y2))
                    self.vecinos[(x2,y2)].add((x1,y1))           

    def bfs(self):
        with open ("niveles.dat", "w") as crear:
            inicio = self.nodos[0]
            encontrados = []
            aux = [inicio]
            niveles = {}         
            niveles[inicio]= 0
            print(inicio[0],inicio[1],niveles[inicio],file=crear)
            visitados= [inicio]
            while aux:
                nodo = aux.pop(0)
                encontrados.append(nodo)
                vecindad = self.vecinos[nodo]
                for vecino in vecindad:
                    if vecino not in visitados:
                        aux.append(vecino)
                        visitados.append(vecino)
                        niveles[vecino]= niveles[nodo]+1
                        print(vecino[0],vecino[1],niveles[vecino], file=crear)
                                   
            print(niveles)
            return encontrados

    def ArchivoGnu(self):
        with open("tarea3.plot","w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'grafica3.eps'", file=archivo)
            print("set xrange [-0.5:10.5]", file=archivo)
            print("set yrange [-0.5:10.5]", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=1
            for key in self.arcos:
                x1 = key[0][0]
                y1 = key[0][1]
                x2 = key[1][0]
                y2 = key[1][1]
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num,x1,y1,x2,y2),file=archivo)
                num+=1
            print("plot 'niveles.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
            print("show arrow", file=archivo)
            print("quit()",file=archivo)
            

########################################################################
            
Nnodos = 50
G = Grafo()
G.CreaNodos()
G.CreaAristas()
G.ArchivoGnu()
G.bfs()
             
#0-gris
#1-morado
#2-verde
#3-celeste
#4-naranja
#5-amarillo
#6-azul
#7-rojo
#8-negro
