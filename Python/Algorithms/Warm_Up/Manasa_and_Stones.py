# Hacker Rank (www.hackerrank.com)
# Manasa and Stones
# author: Nurbek Sakiev

t = int(raw_input())
for i in range(t):
    list_ = []
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    res = a*(n-1)
    list_.append(res)
    for j in range(n-1):
        res = res + abs(b-a)
        list_.append(res)
    print ' '.join(map(str,list_))