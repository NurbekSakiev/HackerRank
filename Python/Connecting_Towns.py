# Hacker Rank (www.hackerrank.com)
# Connecting Towns
# author: Nurbek Sakiev

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    list_ = list(map(int,raw_input().split()))
    res = 1
    for j in xrange(n-1):
        res = res * list_[j]
    print res%1234567
        