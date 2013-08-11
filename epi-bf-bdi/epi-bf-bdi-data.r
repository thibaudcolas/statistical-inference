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
