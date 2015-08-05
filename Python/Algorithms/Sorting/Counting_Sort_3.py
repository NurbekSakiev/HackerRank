// Hacker Rank (www.hackerrank.com)
// Counting_Sort_3
// author: Nurbek Sakiev

t= input()
list_ = []
for i in range(t):
    num, str1 = raw_input().split()
    list_.append(int(num))
    
for j in range(100):
    count = 0
    for k in range(t):
        if j>=list_[k]:
            count+=1
    print count,