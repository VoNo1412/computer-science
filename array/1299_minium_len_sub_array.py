def minSubArrayLen(target, nums):
    size = len(nums) + 1
    total, l = 0, 0

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            size = min(size, r - l + 1)
            total -= nums[l]
            l+=1

    return size if size != len(nums)+1 else 0
        
         
                

print(minSubArrayLen(7,  [2,3,1,2,4,3]))
# print(minSubArrayLen(4,  [1,4,4]))
# print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen(11, [1,2,3,4,5]))
