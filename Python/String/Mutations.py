# Hacker Rank (www.hackerrank.com)
# Mutations
# author: Nurbek Sakiev

string1 = raw_input()
index,char = raw_input().split()
index = int(index)
string1 = list(string1)
string1[index] = char
string1 = ''.join(string1)
print string1