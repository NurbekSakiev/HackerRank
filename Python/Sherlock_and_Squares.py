# Sherlock and Squares
import math

t = int(raw_input())
for i in xrange(t):
    start,end = [int(i) for i in raw_input().split()]
    first = int(math.sqrt(start))
    if (first*first<start):
        first=first+1
    second = int(math.sqrt(end))
    if(first<=second):
        print second-first+1
    else:
        print 0
