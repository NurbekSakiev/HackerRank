// Hacker Rank (www.hackerrank.com)
// Caesar Cipher
// author: Nurbek Sakiev

N = int(raw_input())
str1 = raw_input()
str2 = ""
K = int(raw_input())%26

for i in str1:
    if (ord(i)>=ord('A') and ord(i)<=ord('Z')):
        if(ord(i)+K > ord('Z')):
            str2+=chr(ord(i)+K-26)
        else:
            str2+=chr(ord(i)+K)
    elif(ord(i)>=ord('a') and ord(i)<=ord('z')):
        if(ord(i)+K > ord('z')):
            str2+=chr(ord(i)+K-26)
        else:
            str2+=chr(ord(i)+K)
    else:
        str2+=i
print str2
            

        
        

