# Hacker Rank (www.hackerrank.com)
# Service Lane
# author: Nurbek Sakiev

## Version 1.0

N,T = [int(x) for x in raw_input().split()]
list = [int(x) for x in raw_input().split()]
for l in xrange(T):
    i,j = [int(y) for y in raw_input().split()]
    smallest = 3
    for k in xrange(i, j+1):
        if(list[k]<smallest):
            smallest = list[k]
    print smallest

## Version 2.0 (efficient)

entry = raw_input().split()
N = int(entry[0])
T = int(entry[1])
list = [int(x) for x in raw_input().split()]
for x in xrange(T):
    l = raw_input().split()
    i = int(l[0])
    j = int(l[1])
    print min(list[i:j+1])