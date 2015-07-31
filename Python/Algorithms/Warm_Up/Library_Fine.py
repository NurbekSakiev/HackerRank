// Hacker Rank (www.hackerrank.com)
// Library Fine
// author: Nurbek Sakiev

returned = list(raw_input().split())
taken = list(raw_input().split()) 
fine = 0

if(int(returned[2])-int(taken[2])>0):
    fine = 10000
if(int(returned[1])-int(taken[1])>0 and (int(returned[2])-int(taken[2]))==0):
    fine=500*(int(returned[1])-int(taken[1]))
if ((int(returned[0])-int(taken[0]))>0 and (int(returned[1])-int(taken[1]))==0 and (int(returned[2])-int(taken[2]))==0):
    fine = 15*(int(returned[0])-int(taken[0]))
print fine


