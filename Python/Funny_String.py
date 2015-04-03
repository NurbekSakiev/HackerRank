# Hacker Rank (www.hackerrank.com)
# Funny String
# author: Nurbek Sakiev

t = int(raw_input())
for i in xrange(t):
    word = raw_input()
    reverse = word[::-1]
    funny = 0
    for j in xrange(1,len(word)):
        if abs(ord(word[j])-ord(word[j-1])) == abs(ord(reverse[j])-ord(reverse[j-1])):
            funny = 1
        else:
            funny = 0
            break
    if(funny ==1):
        print "Funny"
    else:
        print "Not Funny"
        
        
    