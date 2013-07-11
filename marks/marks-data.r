#!/usr/bin/env Rscript

marks <- read.csv(file="marks-data.csv",head=T,sep=";")

# An overview of the dataset's structure and size.

str(marks)
summary(marks)


# Central tendency and spread.

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


# Scatter plot.

stripchart(marks$mark~marks$homework, method="jitter", vertical=T, xlab="Homework", ylab="Mark", main="Marks for the two homeworks", pch=3)
points(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato")
lines(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato", lwd=2)


# Student's t-test

t.test(marks$mark~marks$homework,paired=T,alternative="two.sided")

# Prediction

hw1<-marks[marks$homework=="hw1","mark"]
hw2<-marks[marks$homework=="hw2","mark"]

plot(jitter(hw1),jitter(hw2), xlab="First homework", ylab="Secund Homework", ylim=c(0,20))
lines(c(mean(hw1),mean(hw1)),c(0,20),col="tomato")
lines(c(0,20),c(mean(hw2),mean(hw2)),col="tomato")

# Linear model

model <- lm(hw2~hw1)
coef(model)

abline(model, lwd=2, col="red")

summary(model)["adj.r.squared"]
