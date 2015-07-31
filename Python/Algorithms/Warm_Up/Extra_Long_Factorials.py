// Hacker Rank (www.hackerrank.com)
// Extra Long Factorials
// author: Nurbek Sakiev

num = int(raw_input())
fact = 1
for i in range(1,num+1):
    fact*=i
print fact