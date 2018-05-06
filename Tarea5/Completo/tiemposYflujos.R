setEPS()
fma <- read.csv("flujosmaximosAristas.csv", header = FALSE)
tpa <- read.csv("TiempoPercolaArista.csv", header = FALSE)

FMA <- data.frame()
for (d in 1:10){
  FMA <-rbind(FMA,fma[((20*d)-19):(20*d),])
}

p <- seq(5,100,5)
postscript("fma.eps")
boxplot(FMA, xlab= "Porcentaje de aristas removidas", ylab = "Flujo máximo", names=p)
dev.off()

TPA <- data.frame()
for (d in 1:10){
  TPA <-rbind(TPA,tpa[((20*d)-19):(20*d),])
}
postscript("tpa.eps")
boxplot(TPA, xlab= "Porcentaje de aristas removidas", ylab = "Tiempo de ejecución (segundos)", names=p)
dev.off()
##########################################################################

fmn <- read.csv("flujosmaximosNodos.csv", header = FALSE)
tpn <- read.csv("TiempoPercolaNodo.csv", header = FALSE)

FMN <- data.frame()
for (d in 1:10){
  FMN <-rbind(FMN,fmn[((82*d)-81):(82*d),])
}

q <- seq(1,82,1) 
postscript("fmn.eps")
boxplot(FMN, xlab= "Cantidad de nodos removidos", ylab = "Flujo máximo", names=q)
dev.off()
TPN <- data.frame()
for (d in 1:10){
  TPN <-rbind(TPN,tpn[((82*d)-81):(82*d),])
}
pdf("tpn.pdf")
boxplot(TPN, xlab= "Cantidad de nodos removidos", ylab = "Tiempo de ejecución (segundos)", names=q)
graphics.off()
