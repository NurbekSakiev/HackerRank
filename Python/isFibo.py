# is Fibo

from math import *
for _ in range(int(raw_input())):
    n = int(raw_input())
    root1 = sqrt(5 * n**2 + 4)
    root2 = sqrt(5 * n**2 - 4)
    isFibo = root1 % 1 == 0 or root2 % 1 == 0

    if(isFibo):
        print "IsFibo"

    else:
        print "IsNotFibo"