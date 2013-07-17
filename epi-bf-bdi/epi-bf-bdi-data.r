#!/usr/bin/env Rscript

# Loading the dataset

data <- read.csv(file="epi-bf-bdi-data.csv",head=T, sep="\t")

names(data)
attach(data)
dim(data)
