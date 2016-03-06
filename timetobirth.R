#d2g    delai de grossesse en jours 
#indic      1 = grossesse , 0 = censure 
#bmiF      bmi de la femme
#bmiH  bmi de l'homme 
#alcF   nombre de boisson alcolisée par semaine chez la femme 
#alcH     nombre de boisson alcolisée par semaine chez l'homme 
#fumF     1 =  fumeuse,  0=  pas fumeuse
#fumH     1 = fumeur,  0= pas fumeur
#ageF      age en année
#ageH   age en année 
#sperm  spermatozoïdes en million 
#testo     niveau de testosterone 
#Correlation 
library(survival)

d2g<-read.csv("d2g.txt", header = TRUE, sep = " ",na.strings = "<NA>")
summary(d2g)

fit <- survfit(Surv(d2g, indic) ~ 1, data = d2g) 
plot(fit, lty = 2:3) 
legend(100, .8, c("Maintained", "Nonmaintained","toto"), lty = 2:3) 
plot(fit, conf.int=T, lty=3:2, lwd=1,  cex=2, log=T,
     xlab="Délai de grosesse (jours)", ylab="Survie")

lines(fit, lty=3:2, lwd=2,  cex=2)
legend(25, 0.1 , c("control","6-MP"), lty=2:3, lwd=2)
survplot(fit)

reg<-survreg(Surv(d2g, indic) ~ 1, data = d2g,
        dist="exponential")
curve(exp(-(exp(-reg$coef[1]) * x)^(1/reg$scale)),
      col="red", add=TRUE)

reg<-survreg(Surv(d2g, indic) ~ 1, data = d2g,
             dist="weibull")
curve(exp(-(exp(-reg$coef[1]) * x)^(1/reg$scale)),
      col="blue", add=TRUE)
lines(predict(reg,d2g,type="quantile",col="red"))

fit <- survfit(Surv(d2g, indic) ~ fumF, data = d2g) 
plot(fit, lty = 2:3) 
legend(25, 0.1 , c("fumeuse","pas fumeuse"), lty=2:3, lwd=2)
reg<-survreg(Surv(d2g, indic) ~ fumF, data = d2g,
             dist="weibull")
curve(exp(-(exp(-reg$coef[1]) * x)^(1/reg$scale)),
      col="blue", add=TRUE)
fit <- survfit(Surv(d2g, indic) ~ fumH, data = d2g) 
plot(fit, lty = 2:3) 
legend(25, 0.1 , c("fumeur","pas fumeur"), lty=2:3, lwd=2)
reg<-survreg(Surv(d2g, indic) ~ fumH, data = d2g,
             dist="weibull")
curve(exp(-(exp(-reg$coef[1]) * x)^(1/reg$scale)),
      col="blue", add=TRUE)

d2g$bmiFQuant <- cut(d2g$bmiF,breaks=quantile(d2g$bmiF),include.lowest=TRUE)
d2g$bmiHQuant <- cut(d2g$bmiH,breaks=quantile(d2g$bmiH),include.lowest=TRUE)
levels(d2g$bmiFQuant)
levels(d2g$bmiHQuant)

outt=survfit(Surv(d2g,indic) ~bmiFQuant,data=d2g)
plot(outt,lty=1:4,col=1:4,xlab="years",ylab="Probability, KM") ### plusieurs type de lignes
legend(3,0.4,levels(d2g$bmiFQuant),lty=1:4,col=1:4)
title(main="Melanoma data")

outt=survfit(Surv(d2g,indic) ~bmiHQuant,data=d2g)
plot(outt,lty=1:4,col=1:4,xlab="years",ylab="Probability, KM") ### plusieurs type de lignes
legend(3,0.4,levels(d2g$bmiHQuant),lty=1:4,col=1:4)
title(main="Melanoma data")

survdiff(Surv(d2g,indic) ~bmiFQuant,data=d2g)
survdiff(Surv(d2g,indic) ~bmiHQuant,data=d2g)

d2g$alcFQuant <- cut(d2g$alcF,breaks=unique(quantile(d2g$alcF)),include.lowest=TRUE)
d2g$alcHQuant <- cut(d2g$alcH,breaks=quantile(d2g$alcH),include.lowest=TRUE)
levels(d2g$alcFQuant)
levels(d2g$alcHQuant)

outt=survfit(Surv(d2g,indic) ~alcFQuant,data=d2g)
plot(outt,lty=1:4,col=1:4,xlab="years",ylab="Probability, KM") ### plusieurs type de lignes
legend(3,0.4,levels(d2g$alcFQuant),lty=1:4,col=1:4)
title(main="Melanoma data")

outt=survfit(Surv(d2g,indic) ~alcHQuant,data=d2g)
plot(outt,lty=1:4,col=1:4,xlab="years",ylab="Probability, KM") ### plusieurs type de lignes
legend(3,0.4,levels(d2g$alcHQuant),lty=1:4,col=1:4)
title(main="Melanoma data")

survdiff(Surv(d2g,indic) ~alcFQuant,data=d2g)
survdiff(Surv(d2g,indic) ~alcHQuant,data=d2g)
d2g$sperm<-as.numeric(as.character(d2g$sperm))
d2gSperm<-d2g[complete.cases(d2g[,12]),]

d2gSperm$sperm<-as.numeric(as.character(d2gSperm$sperm))
d2gSperm$spermQuant <- cut(d2gSperm$sperm,breaks=unique(quantile(d2gSperm$sperm)),include.lowest=TRUE)

levels(d2gSperm$spermQuant)


outt=survfit(Surv(d2g,indic) ~spermQuant,data=d2gSperm)
plot(outt,lty=1:4,col=1:4,xlab="years",ylab="Probability, KM") ### plusieurs type de lignes
legend(3,0.4,levels(d2gSperm$spermQuant),lty=1:4,col=1:4)
title(main="Melanoma data")


survdiff(Surv(d2g,indic) ~spermQuant,data=d2gSperm)

