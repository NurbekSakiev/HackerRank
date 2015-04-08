# Hacker Rank (www.hackerrank.com)
# Restaurant
# author: Nurbek Sakiev

t = int(raw_input())
for j in xrange(t):
    max_size = 0
    l,b = [int(i) for i in raw_input().split()]
    if(l<b):
        smaller = l
    else:
        smaller = b
    for k in xrange(1, smaller+1,1):
        if(l%k == 0 and b%k == 0):
            max_size = ((l*b)/(k*k))
    print max_size
        