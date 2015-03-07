t = int(raw_input())
for i in range(t):
    l,b = (int(l) for l in raw_input().split(' '))
    if(abs(l*b)%3==0):
        print "YES"
    else:
        print "NO", abs((l*b)%3)