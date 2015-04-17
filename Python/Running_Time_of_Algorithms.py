# Hacker Rank (www.hackerrank.com)
# Running Time of Algorithms
# author: Nurbek Sakiev

N = int(raw_input())
list_ = [int(i) for i in raw_input().split()]
count = 0
for j in range(N-1):
    for k in range(1,N,1):
        if (list_[k-1]>list_[k]):
            value = list_[k]
            list_[k] = list_[k-1]
            list_[k-1] = value
            count = count+1
print count