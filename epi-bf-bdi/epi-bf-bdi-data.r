#!/usr/bin/env Rscript

# Loading the dataset

data <- read.csv(file="epi-bf-bdi-data.csv",head=T, sep="\t")

names(data)
attach(data)
dim(data)

# Overview

summary(data)

# Linear model visualization

plot(jitter(epiImp), jitter(epiE), xlab="Impulsiveness Level", ylab="General Extroversion Level", pch=3)

# Linear model construction

mod <- lm(epiE~epiImp)
summary(mod)

# Mean of the residuals

mean(mod$residuals)

# Gaussian distribution

qqnorm(mod$residuals)
qqline(mod$residuals,col="tomato",lwd=3)

# Homoscedasticity

normResiduals <- rstudent(mod)

plot(jitter(epiImp), normResiduals, pch=3, main="Variable against studentized residuals", xlab="Impulsiveness level", ylab="Residuals")
lines(c(-1,10), c(0,0), lty=2, col="tomato", lwd=3)

plot(jitter(mod$fitted.values), normResiduals, pch=3, main="Predicted values against studentized residuals", xlab="Predicted values", ylab="Residuals")
lines(c(-1,30), c(0,0), lty=2, col="tomato", lwd=3)

# Accounting for gender differences

plot(jitter(epiImp), jitter(epiE), xlab="Impulsiveness Level", ylab="General Extroversion Level", , pch=ifelse(sex=="F",5,15), col=ifelse(sex=="F","red", "blue"))
legend("bottomright", "(x,y)", c("Female", "Male"), pch=c(5,15), col=c("red", "blue"))

mod2 <- lm(epiE~epiImp + sex)
summary(mod2)
