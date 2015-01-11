from matplotlib import pyplot
from numpy import arange
import bisect

def scatterplot(x,y):
    pyplot.plot(x,y,'b.')
    pyplot.xlim(min(x)-1,max(x)+1)
    pyplot.ylim(min(y)-1,max(y)+1)
    pyplot.show()

def barplot(labels,data):
    pos=arange(len(data))
    pyplot.xticks(pos+1.4,labels)
    pyplot.bar(pos,data)
    pyplot.show()

def histplot(data,bins=None,nbins=5):
    if not bins: 
        minx,maxx=min(data),max(data)
        space=(maxx-minx)/float(nbins)
        bins=arange(minx,maxx,space)
    binned=[bisect.bisect(bins,x) for x in data]
    l=['%.1f'%x for x in list(bins)+[maxx]] if space<1 else [str(int(x)) for x in list(bins)+[maxx]]
    displab=[x+'-'+y for x,y in zip(l[:-1],l[1:])]
    barplot(displab,[binned.count(x) for x in range(len(bins)+1)])

def barchart(x,y,numbins=5):
    datarange=max(x)-min(x)
    bin_width=datarange/numbins
    pos=min(x)
    bins=[0 for i in range(numbins+1)]
    for i in range(numbins):
        bins[i]=pos
        pos+=bin_width
    bins[numbins]=max(x)
    binsum=[0 for i in range(numbins)]
    bincount=[0 for i in range(numbins)]
    binaverage=[0 for i in range(numbins)]
    for i in range(numbins):
        for j in range(len(x)):
            if x[j]>=bins[i] and x[j]<bins[i+1]:
                bincount[i]+=1
                binsum[i]+=y[j]
    for i in range(numbins):
        binaverage[i]=binsum[i]/bincount[i]
    barplot(range(numbins),binaverage)

def piechart(labels,data):
    fig=pyplot.figure(figsize=(7,7))
    pyplot.pie(data,labels=labels,autopct='%1.2f%%')
    pyplot.show()

#Write a function to return p as described in the video
#def f(p):
#    return p

#print f(0.3)

#Return the probability of exactly one head in three flips
#def f(p):
#    return p * (1-p) * (1-p)

#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads

#def f(p0,p1,p2):
#    return p0 * p1 + (1-p0) * p2

#Calculate the probability of a positive result given that
#p0=P(C)
#p1=P(Positive|C)
#p2=P(Negative|Not C)

#def f(p0,p1,p2):
#    return p0 * p1 + (1-p0) * (1-p2)

#Return the probability of A condioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 

#def f(p0,p1,p2):
#    return (p0 * p1) / ((p0 * p1) + ((1 - p2) * (1- p0)))

from __future__ import division
class FlipPredictor(object):
    def __init__(self,coins):
        self.coins=coins
        n=len(coins)
        self.probs=[1/n]*n
    def pheads(self):
        return sum(pcoin*p for pcoinp in zip(self.coins,self.probs))

    def update(self,result):
        pheads=self.Pheads()
        if result=='H' :
            self.probs=[pcoin*p/pheads for pcoin,p in zip(self.coins,self.probs)]
        else:
            self.probs[(1-pcoin)*p/(1-pheads) for pcoin,p in zip(self.coins,self.probs)]
#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    return sum(data)/len(data)

#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
def median(data):
   return sorted(data)[(len(data)/2)]

#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    cpt = 0
    for i in range(len(data)):
        c=data.count(data[i])
        if c > cpt:
            mode=data[i]
            cpt=c
    return mode

#Complete the variance function to make it return the variance of a list of numbers
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu = mean(data)
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i] - mu)**2)
    sigma2 = mean(ndata)
    return sigma2

#Complete the stddev function to make it return the standard deviation 
#of a list of numbers
from math import sqrt

data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]


def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])
def stddev(data):
    return sqrt(variance(data))


#Compute the likelihood of observing a sequence of die rolls
#Likelihood is the probability of getting the specific set of rolls 
#in the given order
#Given a multi-sided die whose labels and probabilities are 
#given by a Python dictionary called dist and a sequence (list, tuple, string) 
#of rolls called data, complete the function likelihood
#Note that an element of a dictionary can be retrieved by dist[key] where
#key is one of the dictionary's keys (e.g. 'A', 'Good'). 

def likelihood(dist,data):
    l=1
    for i in data:
        l*=dist[i]
    return l


tests= [(({'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2},'ABCEDDECAB'), 1.024e-07),(({'Good':0.6,'Bad':0.2,'Indifferent':0.2},['Good','Bad','Indifferent','Good','Good','Bad']), 0.001728),(({'Z':0.6,'X':0.333,'Y':0.067},'ZXYYZXYXYZY'), 1.07686302456e-08),(({'Z':0.6,'X':0.233,'Y':0.067,'W':0.1},'WXYZYZZZZW'), 8.133206112e-07)]

for t,l in tests:
    if abs(likelihood(*t)/l-1)<0.01: print 'Correct'
    else: print 'Incorrect'