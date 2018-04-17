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
                self.vecinos[a].append(b)
                self.vecinos[b].append(a)

    def conectaAleatorio(self, p):
        for (x1,y1) in self.nodos:
            for (x2,y2) in self.nodos:
                rand = random.uniform(0,1)
                if rand < p and ((x1,y1),(x2,y2)) not in self.aristas and ((x2,y2),(x1,y1)) not in self.aristas:
                    self.kmax = floor(i/2)
                    u = self.nodos.index((x1,y1))
                    v = self.nodos.index((x2,y2))
                    dis = abs(u-v)
                    if dis > self.kmax:
                        dis2 = i - dis
                        self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis2
                    else:
                        self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis                       
                    self.vecinos[(x1,y1)].append((x2,y2))
                    self.vecinos[(x2,y2)].append((x1,y1))
                        

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
            numvecino = len(self.vecinos[(x,y)]) -1
            for t in range(numvecino):
                print("el vecino es")
                
                self.clustCoef = 0
                h = self.vecinos[(x,y)][t]
                print(h)

                for m in self.vecinos[h]:
                    
                    if m in self.vecinos[(x,y)] and m is not (x,y) and (y,x):
                        print("el vecino del vecino es")
                        print(m)
                        self.clustCoef = self.clustCoef + 1
                        #preguntar si la arista esta en lista
                        #si sí, la cuenta y ,a quitas de la lista la arista encontrada *2
                #print(self.clustCoef)
            dens = 2*self.clustCoef/((numvecino)*(numvecino-1))
            self.densidad.append(dens)
        #print(self.densidad)
        
        
                    

    def graficar(self):
        with open("Tarea4.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'Tarea4.pdf'", file=archivo)
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



i = 6
k = ceil(i/4)
p = 0.1
G = Grafo()
G.agrega(i)
G.conecta(k)
G.conectaAleatorio(p)
G.floyd_warshall()
G.DistanciaCoeficiente()
G.graficar()
