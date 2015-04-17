# Hacker Rank (www.hackerrank.com)
# Cavity Map
# author: Nurbek Sakiev

import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 or j == n-1 or j ==0 or i == n-1:
            print(a[i][j], end = '')
        elif (a[i][j]>a[i-1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1] and a[i][j]>a[i+1][j]):
            print('X',end= '')
        else:
            print(a[i][j],end = '') 
    print()