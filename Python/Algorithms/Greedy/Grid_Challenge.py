// Hacker Rank (www.hackerrank.com)
// Grid Challenge
// author: Nurbek Sakiev

t = input()
possibility = 0
for i in range(t):
    n = input()
    for j in range(n):
        ar = list(raw_input())
        ar = sorted(ar)
        first = ar[0]
        if(first >= last):
            possibility = 1
        last = ar[n-1]
        