# Hacker Rank (www.hackerrank.com)
# Lonely Integer
# author: Nurbek Sakiev

def lonelyinteger(a):
    answer = 0
    for x in b:
        if(b.count(x)==1):
            answer = x
            break
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
