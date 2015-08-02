// Hacker Rank (www.hackerrank.com)
// Time_Conversion
// author: Nurbek Sakiev

# Version 1.0

old = list(raw_input())
if old[8] == 'A':
    if(''.join(old[:2]))=='12':
        old[0] = old[1] = '0'
    new = old[:8]
    new = ''.join(new)
else:
    if(''.join(old[:2]))=='12':
        new = list('12')+old[2:8]
    else:
        add = old[:2]
        add = int(''.join(add))
        new = 12+add
        new = list(str(new))+old[2:8]
    new = ''.join(new)
print new

# Version 2.0

t=raw_input()
a=map(int,t[:-2].split(':'))
t=t[-2:]
if t=='PM' and 1<=a[0]<=11 :
    a[0]+=12
if t=='AM' and a[0]==12 :
    a[0]-=12
a=map(str,a)
for i in range(3) :
    if len(a[i])==1 :
        a[i]='0'+a[i]
print ':'.join(a)
