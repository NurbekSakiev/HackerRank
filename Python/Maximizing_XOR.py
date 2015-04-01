# Maximizing XOR

def  maxXor( l,  r):
    max = 0
    for i in xrange(l,r+1):
        for j in xrange(l,r+1):
            if(max<(i^j)):
                max = i^j
    return max

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

