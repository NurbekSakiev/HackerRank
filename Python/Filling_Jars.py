n,m = (int(i) for i in raw_input().split())
total = 0
for j in range(m):
	a,b,k = (int(i) for i in raw_input().split())
	total = (b-a+1)*k
print (total/n)
