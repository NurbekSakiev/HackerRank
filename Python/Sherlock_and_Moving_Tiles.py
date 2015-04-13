# Hacker Rank (www.hackerrank.com)
# Sherlock and Moving Tiles
# author: Nurbek Sakiev

import math
L,s1,s2 = [int(i) for i in raw_input().split()]
Q = int(raw_input())
for i in xrange(Q):
    q = int(raw_input())
    l = math.sqrt(2*q)
    res = abs(math.sqrt(2*math.pow(L,2))-l)/(abs(s1-s2))
    print format(res, '.20f') 