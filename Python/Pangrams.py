# Hacker Rank (www.hackerrank.com)
# Pangrams
# author: Nurbek Sakiev

from collections import Counter
from collections import OrderedDict

alphabet = 'abcdefghijklmnopqrstuvwxyz'
sentence = raw_input()
sentence = ''.join(e for e in sentence if e.isalnum())      ##join all alphanumeric into one string
a = Counter(sentence)                                       ##convert string into dict
my_list = list(a.keys())                                    ##take the keys of a dict as a list
my_list = map(lambda x: x.lower(),my_list)                  ##apply lower() to all items in a list
my_list = ''.join(OrderedDict.fromkeys(sorted(my_list)))    ##join into ordered string the items(letters) in an array
if alphabet == my_list:
    print "pangram"
else:
    print "not pangram"
