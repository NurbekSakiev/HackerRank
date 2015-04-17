# Hacker Rank (www.hackerrank.com)
# Insertion Sort - Part 1
# author: Nurbek Sakiev

size = int(raw_input())
list1 = [int(i) for i in raw_input().split()]

for j in range(size-1,0,-1):
    if(list1[j]<=list1[j-1]):
        temp = list1[j]
        list1[j] = list1[j-1]
        print ' '.join(map(str,list1))
        list1[j-1] = temp
    else:
        break
        
print ' '.join(map(str,list1))
 
