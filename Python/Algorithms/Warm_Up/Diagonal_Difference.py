// Hacker Rank (www.hackerrank.com)
// Diagonal Difference
// author: Nurbek Sakiev

t = int(raw_input())
sum1=sum2=0
for k in range(t):
    list_ = [int(i) for i in raw_input().split()]
    first, second = list_[k], list_[len(list_)-k-1]
    sum1+=first
    sum2+=second
print abs(sum1-sum2)