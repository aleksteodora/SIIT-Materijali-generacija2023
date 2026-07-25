x<-c(23,21,18,19,24,16,12,21,7,24,6,10,23,22,5)
n<-length(x); n

min<-min(x); min

#medijana
me<-median(x); me

#modus
tx<-table(x)
mo<-as.numeric(names(tx)[tx==max(tx)]); mo

#asr
xn<-mean(x); xn

#uzoracka disperzija
sn2<-sd(x)^2*(n-1)/n; sn2

#standardna devijacija
sn<-sqrt(sn2); sn

#koef spljostenosti i asimetrije
mi4<-mean((x-xn)^4); mi4
mi3<-mean((x-xn)^3); mi3
mi2<-mean((x-xn)^2); mi2

ks<-mi4/mi2^2; ks
ka<-mi3/mi2^(3/2); ka

#treci decil aproksimativnog
treci<-quantile(x, 0.3); treci

#empirijska
#cumsum(table(x))/n
F<-ecdf(x)
F(19.7)

#qqplot
qqnorm(x)
qqline(x)

#histogram
hist(x)
#hist(x, breaks=5)
#hist(x, breaks=c(0,5,10,15,20,25))

pnorm(-0.505)
pnorm(1.362)
qnorm(0.49)
qnorm(0.98)
qnorm(c(0.9, 0.95, 0.975, 0.99, 0.995, 0.999, 0.9995, 0.99995, 0.999995))
rm(list=ls())
