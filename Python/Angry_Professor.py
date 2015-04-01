# Angry Professor

T = int(raw_input())
list = []
for i in xrange(T):
    entry = raw_input().split()
    N = int(entry[0])
    K = int(entry[1])
    count = 0
    list = [int(x) for x in raw_input().split()]
    for j in xrange(N):
        if(list[j]<=0):
            count = count +1
    if (count<K):
        print "YES"
    else:
        print "NO"
    