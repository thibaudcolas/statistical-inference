# Statistical inference applied on students marks

## Variables

- Mark : numerical continuous on [0;20]
- Homework : dichotomous : hw1, hw2

## Distribution

Univariate crossed distribution with each student taking both homework subjects.

Formula : `S51*M2`

102 observations for 51 subjects
All 51 subjects take both M1 and M2

There should be interferences between both activities.

## Overview of the dataset

```r
  > marks <- read.csv(file="marks-data.csv",head=T,sep=";")

  > str(marks)
  'data.frame': 102 obs. of  2 variables:
   $ homework: Factor w/ 2 levels "hw1","hw2": 1 1 1 1 1 1 1 1 1 1 ...
   $ mark    : int  16 15 18 17 16 6 16 13 16 20 ...
  > summary(marks)
   homework      mark      
   hw1:51   Min.   : 0.00  
   hw2:51   1st Qu.:12.25  
            Median :15.00  
            Mean   :13.99  
            3rd Qu.:16.75  
            Max.   :20.00  
```

## Descriptive statistics measures

```r
  > firstHomework <- subset(marks, homework == 'hw1')
  > secundHomework <- subset(marks, homework == 'hw2')

  > mean(firstHomework$mark)
  [1] 14.43137
  > mean(secundHomework$mark)
  [1] 13.54902
  > median(firstHomework$mark)
  [1] 15
  > median(secundHomework$mark)
  [1] 15
  > var(firstHomework$mark)
  [1] 15.3702
  > var(secundHomework$mark)
  [1] 15.01255
  > sd(firstHomework$mark)
  [1] 3.920484
  > sd(secundHomework$mark)
  [1] 3.874603
```

## Scatter plot

The following scatter plot compares the marks of the two homeworks, and outlines their means.

```r
  > stripchart(marks$mark~marks$homework, method="jitter", vertical=T, xlab="Homework", ylab="Mark", main="Marks for the two homeworks", pch=3)
  > points(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato")
  > lines(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato", lwd=2)
```

![Marks scatterplot](marks-scatterplot.png)


## Descriptive analysis

The means of both homework are similar but the distribution of the marks differs : for the first homework, the majority of the marks is comprised between 12 and 20, whereas for the secund one marks are spread between 5 and 20.
