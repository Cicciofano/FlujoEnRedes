dens <- read.csv("DensidadPromedio.csv", header = FALSE)
dis <- read.csv("DistanciaPromedio.csv", header = FALSE)
tiem <- read.csv("tiempos.csv", header = FALSE)

Densidad <- data.frame()
for (d in 1:10){
  Densidad <-rbind(Densidad,dens[((10*d)-9):(10*d),])
}
DensidadPromedio <- data.frame()
for (d in 1:10){
  DensidadPromedio <- rbind(DensidadPromedio, mean(as.numeric(Densidad[d,])))
}

Distancia <- data.frame()
for (d in 1:10){
  Distancia <-rbind(Distancia,dis[((10*d)-9):(10*d),])
}
DistanciaPromedio <- data.frame()
for (d in 1:10){
  DistanciaPromedio <- rbind(DistanciaPromedio, mean(as.numeric(Distancia[d,])))
}

p <- seq(0.05,0.5,.05)

pdf("td.pdf")
plot(p,rev(DensidadPromedio[,1]), type = "l", ylim = c(0,0.8), col="red", ylab = "Densidades")
par(new=TRUE)
plot(p,DistanciaPromedio[,1], type = "l", ylim = c(0,0.8),xaxt = "n", yaxt = "n",
     ylab = "", xlab = "", col="blue")
axis(side = 4)
mtext("Distancia", side = 4, line = 3)
legend("topright", c("Distancias", "Densidades"),
       col = c("blue", "red"), lty = c(1, 1))
graphics.off()

Tiempos <- data.frame()
for (t in 1:10){
  Tiempos <-rbind(Tiempos,tiem[((5*t)-4):(5*d),])
}
