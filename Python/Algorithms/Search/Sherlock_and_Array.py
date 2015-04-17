# Hacker Rank (www.hackerrank.com)
# Sherlock and Array
# author: Nurbek Sakiev

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    list_ = list(map(int,raw_input().split()))
    if(n==1):
        print "YES"
    elif(n==2):
        print "NO"
    else:
        left, right = 0, sum(list_[1:])
        for j in xrange(1,n-1):
            left,right = left+list_[j-1],right-list_[j]
            if(left == right):
                print "YES"
                break
        else:
            print "NO"