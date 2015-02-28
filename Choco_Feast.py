# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    dollars,chock_price,wrap_change = [int(x) for x in raw_input().split(' ')]
    answer = 0
    
    # write code to compute answer
    chocks = wrapper = dollars/chock_price #counting the number of chocks(wrappers) can be bought
    while (wrapper>=wrap_change):          
        change = wrapper/wrap_change       #change wrappers to chocks
        chocks +=change                    #add them to total
        wrapper %=wrap_change              #how many wrappers left after change
        wrapper +=change                   #add wrappers left after change and new chocko wrappers
    print chocks

