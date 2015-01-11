import plotting

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


def test(coins,flips):
    f=FlipPredictor(coins)
    guesses=[]
    for flip in flips:
        f.update(flip)
        guesses.append(f.pheads())
    return guesses

def maxdiff(l1,l2):
    return max([abs(x-y) for x,y in zip(l1,l2)])

testcases=[
(([0.5,0.4,0.3],'HHTH'),[0.4166666666666667, 0.432, 0.42183098591549295, 0.43639398998330553]),
(([0.14,0.32,0.42,0.81,0.21],'HHHTTTHHH'),[0.5255789473684211, 0.6512136991788505, 0.7295055220497553, 0.6187139453483192, 0.4823974597714815, 0.3895729901052968, 0.46081730193074644, 0.5444108434105802, 0.6297110187222278]),
(([0.14,0.32,0.42,0.81,0.21],'TTTHHHHHH'),[0.2907741935483871, 0.25157009005730924, 0.23136284577678012, 0.2766575695593804, 0.3296000585271367, 0.38957299010529806, 0.4608173019307465, 0.5444108434105804, 0.6297110187222278]),
(([0.12,0.45,0.23,0.99,0.35,0.36],'THHTHTTH'),[0.28514285714285714, 0.3378256513026052, 0.380956725493104, 0.3518717367468537, 0.37500429586037076, 0.36528605387582497, 0.3555106542906013, 0.37479179323540324]),
(([0.03,0.32,0.59,0.53,0.55,0.42,0.65],'HHTHTTHTHHT'),[0.528705501618123, 0.5522060353798126, 0.5337142767315369, 0.5521920592821695, 0.5348391689038525, 0.5152373451083692, 0.535385450497415, 0.5168208803156963, 0.5357708613431963, 0.5510509656933194, 0.536055356823069])]

for inputs,output in testcases:
    if maxdiff(test(*inputs),output)<0.001:
        print 'Correct'
    else: print 'Incorrect'
