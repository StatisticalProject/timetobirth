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

library(surv0ival)

d2g<-read.csv("d2g.txt", header = TRUE, sep = " ",na.strings = "<NA>")
summary(d2g)

fit <- survfit(Surv(d2g, indic) ~ 1, data = d2g) 
plot(fit, lty = 2:3) 
legend(100, .8, c("Maintained", "Nonmaintained"), lty = 2:3) 
plot(fit, conf.int=T, lty=3:2, lwd=1,  cex=2, log=T,
     xlab="Délai de grosesse (jours)", ylab="Survie")

lines(fit, lty=3:2, lwd=2,  cex=2)
legend(25, 0.1 , c("control","6-MP"), lty=2:3, lwd=2)
survplot(fit)
