// Hacker Rank (www.hackerrank.com)
// Quicksort 1 - Partition
// author: Nurbek Sakiev

t= input()
list_ = [int(i) for i in raw_input().split()]
list1 = []
list2 = []
p = list_[0]
for j in list_:
    if (j < p):
        list1.append(j)
    else:
        list2.append(j)
print' '.join(map(str, list1))+" "+' '.join(map(str, list2))
    
