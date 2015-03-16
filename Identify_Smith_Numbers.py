n = int(raw_input())
j = 2
total = 0
x=[int(i) for i in str(n)]
sumX = sum(x)
while n!=1:
    if(n%j==0):
        n = n / j
        if(j>9):
            o=[int(i) for i in str(j)]
            sumO = sum(o)
            total = total+sumO
        else:
            total = total + j
    else:
        j = j + 1
if (total == sumX):
    print "1"