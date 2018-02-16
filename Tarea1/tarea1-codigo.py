from random import random
import math
n=30
m=math.ceil(n/5)
p=1
nodos=[]
aristas=[]

for t in range(n):
    x=random()
    y=random()
    nodos.append((x,y))
        
def distancia(p,q):
    return ((((p[0]-q[0])**2)+((p[1]-q[1])**2))**(1/2))

r=0.45
with open ("nodosa.dat", "w") as crear:
    t=0
    for(x2,y2) in nodos[0:n+1]:
        print(x2,y2,t,file=crear)
    t=1
    for(x1,y1) in nodos[0:m]:
        print(x1,y1,t, file=crear)
        t =t+1
    t=1
    for(x1,y1) in nodos[0:m]:
        for(x2,y2) in nodos[m:n]:
            if distancia((x1,y1),(x2,y2))<r:
                aristas.append((x1,y1,x2,y2))
                print(x2,y2,t, file=crear)
        t=t+1
    
with open("prueba1a.plot","w") as archivo:
    print("set term png", file=archivo)
    print("set output 'graficaN30.png'", file=archivo)
    print("set xrange [0:1]", file=archivo)
    print("set yrange [0:1]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    num=1
    for a in aristas:
        (x1,y1,x2,y2)=a
        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num,x1,y1,x2,y2),file=archivo)
        num+=1
    print("show arrow", file=archivo)
    print("plot 'nodosa.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
    print("quit()",file=archivo)

        
