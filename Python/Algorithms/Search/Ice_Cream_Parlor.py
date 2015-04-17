# Hacker Rank (www.hackerrank.com)
# Ice Cream Parlor
# author: Nurbek Sakiev

# Version 1.0

t = int(raw_input())
first, second = 0,0

for i in xrange(t):
    money = int(raw_input())
    num_ind = int(raw_input())
    temp_list = raw_input().split()
    for j in xrange(len(temp_list)-1):
        for k in xrange(j+1, len(temp_list),1):
            
            if (int(temp_list[j])+int(temp_list[k])) == money:
                first, second = j+1, k+1
                break
    print first, second 

# Version 2.0 (more efficient)
import sys

t = int(sys.stdin.readline())
    
for i in range(t):
    money = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))

    for j, c in enumerate(C[:-1]):
        for k in range(j + 1, len(C)):
            if C[k] == money - c:
                print j + 1, k + 1
                break