def arrayPairSum(nums):
    # 1, 2, 3, 4 => [(1, 2), (3, 4)] => (1, 3) = 4
    # 1, 2, 2, 5, 6, 6 => [(1, 2), (2, 5), (6, 6)] => (1, 2, 6) = 9
    nums.sort()
    return sum(nums[::2])        
    
    
print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([6,2,6,5,1,2]))
