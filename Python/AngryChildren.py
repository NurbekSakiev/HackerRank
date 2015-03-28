n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
best = candies[-1]
for i in range(n-k+1):
    if(candies[i+k-1]-candies[i] < best):
        best = candies[i+k-1]-candies[i]
        
print best