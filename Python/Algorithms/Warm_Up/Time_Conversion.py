// Hacker Rank (www.hackerrank.com)
// Time_Conversion
// author: Nurbek Sakiev

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