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

#The code below this line tests your implementation. 
#You need not change it
#You may add additional test cases or otherwise modify if desired
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