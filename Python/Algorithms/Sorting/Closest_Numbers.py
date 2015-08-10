// Hacker Rank (www.hackerrank.com)
// Closest_Numbers
// author: Nurbek Sakiev

t= input()
ar = [int(i) for i in raw_input().split()]
ar = sorted(ar)
new_ar = []
smallest = abs(ar[0]-ar[1])
for i in range(1,t-2):
    if (abs(ar[i]-ar[i+1]) < smallest):
        new_ar = []
        smallest = abs(ar[i]-ar[i+1])
        new_ar.append(ar[i])
        new_ar.append(ar[i+1])
    elif (abs(ar[i]-ar[i+1]) == smallest):
        new_ar.append(ar[i])
        new_ar.append(ar[i+1])
    else:
        continue
print ' '.join(map(str,new_ar))