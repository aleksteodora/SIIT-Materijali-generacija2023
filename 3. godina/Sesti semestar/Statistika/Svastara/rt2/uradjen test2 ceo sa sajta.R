podaci<-read.csv("tips.csv")
View(podaci)

#--PRVI ZADATAK--
#A grupa
manje_od_2<-sum(podaci$tip<2)
uk<-length(podaci$tip)
prop.test(manje_od_2,uk,0.15,correct=FALSE)
binom.test(manje_od_2,uk,.15)

#B grupa
napojnicaM<-podaci$tip[podaci$sex=="Male"]
t.test(napojnicaM, mu=3.5, alternative="greater")

#C grupa
tipM<-podaci$tip[podaci$sex=="Male"]
tipZ<-podaci$tip[podaci$sex=="Female"]
var.test(tipM,tipZ)
t.test(tipM, tipZ, alternative="greater") #po potrebi se doda i ,var.equal=TRUE

#--DRUGI ZADATAK--
#A grupa
chisq.test(matrix(c(38,30,60,65,68,109,35,28,67),3,3))

#B grupa
ks.test(podaci$bill, 'pnorm', 20, 9)
ks.test(podaci$bill, 'pnorm', 20, 9)$statistic*sqrt(length(podaci$bill))

#C grupa
m<-c(1.5,2.5,3.5,5)
pm<-pnorm(m,3,1.4)
p<-c(pm,1)-c(0,pm); round(p,4)
mi<-c(floor(min(podaci$tip)),m,ceiling(max(podaci$tip)))
fi<-hist(podaci$tip, mi)$counts; fi
chisq.test(fi,p=p)

#--TRECI ZADATAK--
#A grupa
boxplot(bill~day,data=podaci) #trebalo bi
podaci$day=as.factor(podaci$day) #vazno
summary(podaci$day)
anova(lm(bill ~ day, data = podaci)) #vazno

#B grupa
boxplot(tip~day, data=podaci)
anova(lm(tip~day, data=podaci))

#C grupa
model<-lm(tip~bill+size,data=podaci)
summary(model)
lm(tip~bill+size,data=podaci)$coeficients%*%c(1,35,4)
