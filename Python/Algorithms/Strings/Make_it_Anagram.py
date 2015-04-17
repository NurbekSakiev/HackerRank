# Hacker Rank (www.hackerrank.com)
# Make it Anagram
# author: Nurbek Sakiev

from collections import Counter

def anagram(a,b):
    dict_a = Counter(a)
    dict_b = Counter(b)
    return sum([abs(dict_a[i]- dict_b[i]) for i in set(a) | set(b)])

if __name__ == '__main__':
    a = raw_input()
    b = raw_input()
    print anagram(a,b)