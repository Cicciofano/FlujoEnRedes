from random import random
from math import ceil, floor, sqrt
import time

def distancia(p,q):
    return sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))
def pmedio(p,q):
    return ((p[0]+q[0])/2),((p[1]+q[1])/2)

class Grafo:
    def __init__(self, prob = 1, radio = 4.5):
        self.n = Nnodos
        self.m = ceil(Nnodos/5)
        self.p = prob
        self.r = radio
        self.nodos = []
        self.puntomedio = []
        self.pesos = []
        self.colores = []
        self.arcos = dict()
        
    def CreaNodos(self):
        for t in range(self.n):
            x=10*random()
            y=10*random()
            self.nodos.append((x,y))
            
    def CreaAristas(self):
        if dirigido is 0:
            with open ("ArcosNoDirigidos.dat", "w") as crear:
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
                            self.puntomedio.append(pmedio((x1,y1),(x2,y2)))
                            self.puntomedio.append(pmedio((x2,y2),(x1,y1)))
                            self.pesos.append(ceil(distancia((x1,y1),(x2,y2))))
                            self.pesos.append(ceil(distancia((x2,y2),(x1,y1))))
                            self.colores.append(t)
                            self.colores.append(t)
                            self.arcos[(x1,y1),(x2,y2)] = ceil(distancia((x1,y1),(x2,y2)))
                            self.arcos[(x2,y2),(x1,y1)] = ceil(distancia((x1,y1),(x2,y2)))
                            print(x2,y2,t, file=crear)
                        
                    t=t+1
        else:
            with open ("ArcosDirigidos.dat", "w") as crear:
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
                            self.puntomedio.append(pmedio((x1,y1),(x2,y2)))
                            self.pesos.append(ceil(distancia((x1,y1),(x2,y2))))
                            self.colores.append(t)
                            self.arcos[(x1,y1),(x2,y2)] = ceil(distancia((x1,y1),(x2,y2)))
                            print(x2,y2,t, file=crear)
                    t=t+1
            
    def floyd_warshall(self): 
        d = {}
        for v in range (len(self.nodos)):
            dot=self.nodos[v]
            d[(dot, dot)] = 0 # distancia reflexiva es cero
            u=0
            for key in self.arcos: # para vecinos, la distancia es el peso
                x1 = key[0][0]
                y1 = key[0][1]
                x2 = key[1][0]
                y2 = key[1][1]
                p1=(x1,y1)
                p2=(x2,y2)
                d[(p1,p2)] = self.pesos[u]
                u+=1
                
        for intermedio in range (len(self.nodos)):
            for desde in range (len(self.nodos)):
                for hasta in range (len(self.nodos)):
                    di = None
                    if (self.nodos[desde], self.nodos[intermedio]) in d:
                        di = d[(self.nodos[desde], self.nodos[intermedio])]
                    ih = None
                    if (self.nodos[intermedio], self.nodos[hasta]) in d:
                        ih = d[(self.nodos[intermedio], self.nodos[hasta])]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (self.nodos[desde], self.nodos[hasta]) not in d or c < d[(self.nodos[desde], self.nodos[hasta])]:
                            d[(self.nodos[desde], self.nodos[hasta])] = c # mejora al camino actual
        print(d)
        return d

    def camino(self): # construcción de un camino aumentante
        cola = [self.s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for ((w, v)) in self.arcos:
                if w == u and v not in cola and v not in usados:
                    actual = self.flujo.get((u, v), 0)
                    dif = self.arcos[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if self.t in usados:
           return camino
        else: # no se alcanzó
            return None
    
    def ford_fulkerson(self): # algoritmo de Ford y Fulkerson
        self.s = self.nodos[0]
        self.t = self.nodos[self.m-1]
        if self.s == self.t:
            return 0
        maximo = 0
        self.flujo = dict()
        while True:
            aum = self.camino()
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
            while u in aum:
                v = aum[u][0]
                actual = self.flujo.get((v, u), 0) # cero si no hay
                inverso = self.flujo.get((u, v), 0)
                self.flujo[(v, u)] = actual + incr
                self.flujo[(u, v)] = inverso - incr
                u = v
            maximo += incr
        print(maximo)
        return maximo

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
                (xm,ym) = self.puntomedio[num-1]
                col = self.colores[num-1]                
                if dirigido is 1:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size .5,10 lt {:f} lw 1".format(num,x1,y1,x2,y2,col),file=archivo)
                else:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:f} lw 1".format(num,x1,y1,x2,y2,col),file=archivo)
                if pesos is 1:
                    p = self.arcos[key]
                    print("set label font ',10' '{:d}' at {:f}, {:f} tc lt {:f}".format(p, xm, ym, col), file = archivo)
                num+=1
            if dirigido is 0:
                print("plot 'ArcosNoDirigidos.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
                print("show arrow", file=archivo)
                print("quit()",file=archivo)
            else:
                print("plot 'ArcosDirigidos.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
                print("show arrow", file=archivo)
                print("quit()",file=archivo)

########################################################################

dirigido = 1 # no dirigido = 0 / dirigido = 1
pesos = 1    # sin pesos   = 0 / con pesos =1
if dirigido is 0:
    with open("tiemposND.csv","w") as archivo:
        start_time = time.clock()
        Nnodos = 6
        G = Grafo()
        G.CreaNodos()
        G.CreaAristas()
        G.ArchivoGnu()
        G.floyd_warshall()
        G.ford_fulkerson()
        print (time.clock() - start_time, file=archivo)
else:
    with open("tiemposD.csv","w") as archivo:
        start_time = time.clock()
        Nnodos = 6  
        G = Grafo()
        G.CreaNodos()
        G.CreaAristas()
        G.ArchivoGnu()
        G.floyd_warshall()
        G.ford_fulkerson()
        print (time.clock() - start_time, file=archivo)

             
#0-gris
#1-morado
#2-verde
#3-celeste
#4-naranja
#5-amarillo
#6-azul
#7-rojo
#8-negro
