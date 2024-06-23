def pivotIndex(nums):
    if len(nums) < 0: return;

    left = totalRight = 0;
    for num in nums: totalRight += num;

    for index, num in enumerate(nums): 
        if left == totalRight - left - num:
            return index;
    
        left += num;

    return -1;


print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
