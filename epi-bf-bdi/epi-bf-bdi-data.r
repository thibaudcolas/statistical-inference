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
