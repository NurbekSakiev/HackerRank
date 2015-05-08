# Hacker Rank (www.hackerrank.com)
# The Time in Words
# author: Nurbek Sakiev

time_words = {"one":1,"two":2,"three":3,'four':4,"five":5,"six":6,"seven":7,'eight':8,"nine":9,"ten":10,
            "eleven":11,'twelve':12,"thirteen":13,"fourteen":14,"quarter":15,'sixteen':16,"seventeen":17,
            "eighteen":18,'nineteen':19,"twenty":20,"twenty one":21,"twenty two":22,"twenty three":23,
            "twenty four":24,"twenty five":25,"twenty six":26,"twenty seven":27,"twenty eight":28, "twenty nine":29,"half":30}
H = int(raw_input())
M = int(raw_input())
m,h = M,H
hour = ''
minutes = ''

if (M > 30):
    m = 60 - m
    h = h+1
for k,v in time_words.iteritems():
    if(v == h):
        hour = '' + k

for k,v in time_words.iteritems():
    if (v == m):
        minutes = ''+k
        
if (M == 0):
    print hour+" o' clock"
elif (M <= 15):
    print 'quarter past '+ hour
elif (M == 30):
    print minutes+' past '+ hour
elif (M == 45):
    print minutes+' to '+ hour
elif (M <=14 or M <= 29 ):
    print minutes+' minutes past '+ hour
else:
    print minutes+' minutes to '+ hour

