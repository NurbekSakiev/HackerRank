# Song of Pi
import string
T = int(raw_input())
pi = "31415926535897932384626433833"
for i in xrange(T):
    my_str = raw_input().split()
    current = 0
    check = 0
    list = []
    for j in my_str:
        list.append(str(len(j)))
        
    check = ''.join(list)
    if(check==pi[:len(list)]):
        print "It's a pi song."
    else:
        print "It's not a pi song."