from random import random, normalvariate,expovariate, randint
from math import ceil, floor, sqrt

def distancia(p,q):
    return (abs(q[0]-p[0])+ abs(q[1]-p[1]))

class Grafo:  
    def __init__(self):
        self.k = k
        self.p = p
        self.contador = 0
        self.nodos = dict()
        self.aristas = dict()
        self.pesos = []
        self.colores = []
        
    def CreaNodos(self):
        n=0
        for t in range(1,k+1):
            for tt in range(1,k+1):
                self.nodos[n+1] = (tt,t)
                n=n+1

    def NuevosNodos(self):
        with open ("cuadricula.dat", "w") as crear:
            q = randint(2,(k*k)-1)
            del self.nodos[q]
            for w in self.nodos:
                x=self.nodos[w][0]
                y=self.nodos[w][1]
                print(x,y, file=crear)
            
       
    def CreaAristas(self,l):
        with open ("nodos.dat", "w") as crear:
            for n in (self.nodos):
                #print(n)
                for nn in (self.nodos):
                    if n is not nn and distancia(self.nodos[n], self.nodos[nn]) < l+1:        
                        self.aristas[self.nodos[n],self.nodos[nn]] = self.aristas[self.nodos[nn],self.nodos[n]] = floor(normalvariate(2, .5))+1
            #este es para las aleatorias
            for n in (self.nodos):
                if self.nodos[n] is not self.nodos[k*k]:
                    for nn in (self.nodos):
                        if self.nodos[nn] is not self.nodos[1]:
                            if n is not nn:
                                aleatorio = random()
                                if aleatorio < self.p and (self.nodos[n],self.nodos[nn]) not in self.aristas:
                                    self.contador = self.contador +1
                                    self.aristas[self.nodos[n],self.nodos[nn]] = ceil(expovariate(1/20))
            print(self.contador)
            print(self.aristas, file=crear)

    def camino(self): # construcción de un camino aumentante
        cola = [self.s]
        usados = set()
        self.caminata = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for ((w, v)) in self.aristas:
                if w == u and v not in cola and v not in usados:
                    actual = self.flujo.get((u, v), 0)
                    dif = self.aristas[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        self.caminata[v] = (u, dif)
        if self.t in usados:
            return self.caminata
        else: # no se alcanzó
            return None
    
    def FF(self): # algoritmo de Ford y Fulkerson
        self.s = self.nodos[1]
        self.t = self.nodos[k*k]
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
        with open("tarea5.plot","w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'tarea5.eps'", file=archivo)
            print("set xrange [0: {:d}]".format(k+1), file=archivo)
            print("set yrange [0: {:d}]".format(k+1), file=archivo)
            print("set pointsize .5", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)      
            num=1
            conteo=1
            for a in self.aristas:
                p1=a[0]
                p2=a[1]
                x1=p1[0]
                y1=p1[1]
                x2=p2[0]
                y2=p2[1]
                if conteo < len(self.aristas)-(self.contador-1):
                    print("set arrow {:d} from {:d}, {:d} to {:d}, {:d} nohead".format(num,x1,y1,x2,y2),file=archivo)
                else:
                    print("set arrow {:d} from {:d}, {:d} to {:d}, {:d} head filled size .5,10 lt 4 lw 2".format(num,x1,y1,x2,y2),file=archivo)                    
                num+=1
                conteo+=1
            print("show arrow", file=archivo)
            print("plot 'cuadricula.dat' using 1:2 with points pt 5", file=archivo)
            print("quit()",file=archivo)

k = 5
l = 3
p = 0.001
percolacion = 1
G=Grafo()
G.CreaNodos()
G.NuevosNodos()
G.CreaAristas(l)
G.FF()
G.ArchivoGnu()
