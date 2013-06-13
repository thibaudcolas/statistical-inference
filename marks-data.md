# Statistical inference applied on students marks

## Variables

Note : variable numérique quantitative discrète 
Domaine : [0;20]

Devoir : variable qualitative ordinale (? nominale)
Deux valeurs : dev1, dev2

## Plan de l'étude

Plan monofactoriel croisé, groupes appariés

Formule : S51*M2

102 données pour 51 sujets
Les 51 sujets passent M1 et M2

Interférences d'une activité à l'autre

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

## Statistiques descriptives indices

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

## Pseudo-dispersion

```r
  > stripchart(marks$mark~marks$homework, method="jitter", vertical=T, xlab="Homework", ylab="Mark", main="Marks for the two homeworks", pch=3)
  > points(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato")
  > lines(c(mean(firstHomework$mark), mean(secundHomework$mark)), pch=3, col="tomato", lwd=2)
```

## Descriptive analysis

Les moyennes des deux devoirs sont relativement similaires mais la distribution des notes est différente : pour le premier devoir, l'essentiel des notes est compris entre 12 et 20, alors que les notes du second devoir sont réparties entre 5 et 20.
