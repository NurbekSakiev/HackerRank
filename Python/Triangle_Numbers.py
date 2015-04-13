# Hacker Rank (www.hackerrank.com)
# Triangle Numbers
# author: Nurbek Sakiev

t =int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    if(n<3):
        print -1
    elif(n%2 == 1):
        print 2
    elif(n%4 == 0):
        print 3
    else:
        print 4
       