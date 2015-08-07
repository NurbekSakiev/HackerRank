// Hacker Rank (www.hackerrank.com)
// Find the Median
// author: Nurbek Sakiev

t = input()
ar = [int(i) for i in raw_input().split()]
ar = sorted(ar)
median = ar[t/2]
print median
    