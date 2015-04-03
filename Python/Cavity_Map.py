# Cavity Map

n = int(raw_input())
for i in xrange(n):
    nums = raw_input()
    nums = [int(i) for i in nums]
    for j in xrange(1, len(nums)-1):
        if(nums[j]>nums[j-1] and nums[j]>nums[j+1]):
            nums[j] = "X"
    print ''.join(map(str, nums))
        