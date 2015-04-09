# Hacker Rank (www.hackerrank.com)
# Handshake
# author: Nurbek Sakiev

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    res = 1
    for j in xrange(n,n-2,-1):
        res = res*j
    print res/2