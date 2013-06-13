#!/usr/bin/env Rscript

marks <- read.csv(file="marks-data.csv",head=T,sep=";")

# An overview of the dataset's structure and size.

str(marks)
summary(marks)

firstHomework <- subset(marks, homework == 'hw1')
secundHomework <- subset(marks, homework == 'hw2')

mean(firstHomework$mark)
mean(secundHomework$mark)
median(firstHomework$mark)
median(secundHomework$mark)
var(firstHomework$mark)
var(secundHomework$mark)
sd(firstHomework$mark)
sd(secundHomework$mark)
