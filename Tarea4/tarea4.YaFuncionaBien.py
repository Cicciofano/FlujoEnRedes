from random import random
from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, random
import time, random

class Grafo:

    def __init__(self):
        self.dis = dict()
        self.vecinos = dict()
        self.aristas = dict()
        self.nodos = []
        

    def agrega(self, i):
        with open("NodosWarshall.dat", "w") as crear:
            centro = (0.5, 0.5)
            radio = 0.4
            angulo = (360/i)*(pi/180)
            for n in range(1, i+1):
                x = radio*cos(angulo*n) + centro[0]
                y = radio*sin(angulo*n) + centro[1]
                self.nodos.append((x,y))
                print(x, y, file = crear)
                if not (x, y) in self.vecinos:
                    self.vecinos[(x,y)] = []
          

    def conecta(self, k):
        for r in range(1,k+1):
            for j in range(0,i):
                a = self.nodos[j]
                b = self.nodos[j-r]
                self.aristas[(a,b)] = self.aristas[(b,a)] = r
                if not a in self.vecinos[b]:
                    if a is not b:
                        if b is not a:
                            self.vecinos[b].append(a)
                if not b in self.vecinos[a]:
                    if b is not a:
                        if a is not b:
                            self.vecinos[a].append(b)

    def conectaAleatorio(self, p):
        for (x1,y1) in self.nodos:
            for (x2,y2) in self.nodos:
                #if (x1,y1) is not (x2,y2):
                rand = random.uniform(0,1)
                if rand < p:
                    if ((x1,y1),(x2,y2)) not in self.aristas:
                        if ((x2,y2),(x1,y1)) not in self.aristas:
                            self.kmax = floor(i/2)
                            u = self.nodos.index((x1,y1))
                            v = self.nodos.index((x2,y2))
                            if u is not v:
                                dis = abs(u-v)
                                print("huele a canela")
                                print(u, v, dis)
                                if dis > self.kmax:
                                    dis2 = i - dis
                                    self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis2 #para impares
                                else:
                                    self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis #para pares porque coincide
                                if (x1,y1) not in self.vecinos[(x2,y2)]:
                                    if (x1,y1) is not (x2,y2):
                                        if (x2,y2) is not (x1,y1):
                                            self.vecinos[(x2,y2)].append((x1,y1))
                                if (x2,y2) not in self.vecinos[(x1,y1)]:
                                    if (x2,y2) is not (x1,y1):
                                        if (x1,y1) is not (x2,y2):
                                            self.vecinos[(x1,y1)].append((x2,y2))
                            
                        

    def floyd_warshall(self):
        self.d = {}
        for (x,y) in self.nodos:
            self.d[((x,y),(x,y))] = 0 # distancia reflexiva es cero
            for u in self.vecinos[(x,y)]: # para vecinos, la distancia es el peso
                self.d[((x,y),u)] = self.aristas[((x,y),u)]
        for intermedio in self.nodos:
            for desde in self.nodos:
                for hasta in self.nodos:
                    di = None
                    if (desde, intermedio) in self.d:
                        di = self.d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in self.d:
                        ih = self.d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in self.d or c < self.d[(desde, hasta)]:
                            self.d[(desde, hasta)] = c # mejora al camino actual
        return self.d

    def DistanciaCoeficiente(self):
        self.sumDis = 0
        for u in self.d:
            self.sumDis = self.sumDis + self.d[u]
        self.argDis = self.sumDis/len(self.d)
        #print(self.argDis)

        self.densidad = []
        #guardar en lista todas las aristas originales
        for (x,y) in self.nodos:
            #print("nuevo nodo")
            #print((x,y))
            #print("las aristas de los vecinos son")
            self.lpq = []
            numvecino = len(self.vecinos[(x,y)])
            self.clustCoef2=0
            for t in range(0,numvecino-1):
                self.clustCoef = 0
                h = self.vecinos[(x,y)][t]
                if (x,y) is not h:
                    for m in self.vecinos[h]:
                        if (x,y) is not m:
                            if m is not h:
                                if h is not m:
                                    if h is not (x,y):
                                        if m is not (x,y):
                                            if m in self.vecinos[(x,y)]:
                                                if (h,m) not in self.lpq:
                                                    self.lpq.append((h,m))
                                                if (m,h) not in self.lpq:
                                                    self.lpq.append((m,h))
                                                    self.clustCoef = self.clustCoef + 1
             #                                   print((h,m))
              #  print(self.clustCoef)
                self.clustCoef2 = self.clustCoef2 + self.clustCoef  
            #print("lala")
            #print(self.clustCoef2)
            #print(numvecino)
            dens = (self.clustCoef2)/(((numvecino)*(numvecino-1))/2)
            self.densidad.append(dens)
        print(self.densidad)
        
        
                    

    def graficar(self):
        with open("Tarea4.plot","w") as archivo:
             print("set term eps", file=archivo)
             print("set output 'Tarea4.eps'", file=archivo)
             print("set xrange [-.1:1.1]", file=archivo)
             print("set yrange [-.1:1.1]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 p = self.aristas[key]
                 if p > k:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'NodosWarshall.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)



i = 10
k = ceil(i/4)
p = 0.1
G = Grafo()
G.agrega(i)
G.conecta(k)
G.conectaAleatorio(p)
G.floyd_warshall()
G.DistanciaCoeficiente()
G.graficar()
