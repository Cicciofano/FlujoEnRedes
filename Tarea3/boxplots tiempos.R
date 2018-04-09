D <- read.csv("tiemposD.csv", header = FALSE)
ND <- read.csv("tiemposND.csv", header = FALSE)

tiemposD <- data.frame()
for (d in 1:10){
  tiemposD<-rbind(tiemposD,D[((30*d)-29):(30*d),])
}
pdf("td.pdf")
boxplot(t(tiemposD),ylim=c(0,4.5), ylab=("Segundos"), xlab=("Nodos"), xaxt="n", main=("Grafos dirigidos"))
axis(1, at=1:10, labels=seq(10,100,10))
par(new=TRUE)
plot(exp, xlab="", ylab="", col="blue", lwd=3, xaxt="n", yaxt="n", ylim=c(1,4), xlim = c(0,1))
legend("topleft", inset=.02, c("Curva exponencial"), fill=topo.colors(3), horiz=TRUE, cex=0.8)
tiemposND <- data.frame()
for (nd in 1:10){
  tiemposND<-rbind(tiemposND,ND[((30*nd)-29):(30*nd),])
}
pdf("tnd.pdf")
boxplot(t(tiemposND), ylim=c(0,4.5),ylab=("Segundos"), xlab=("Nodos"), xaxt="n", main=("Grafos no dirigidos"))
axis(1, at=1:10, labels=seq(10,100,10))
par(new=TRUE)
plot(exp, xlab="", ylab="", col="blue", lwd=3, xaxt="n", yaxt="n", ylim=c(1,3))
legend("topleft", inset=.02, c("Curva exponencial"), fill=topo.colors(3), horiz=TRUE, cex=0.8)
graphics.off()
