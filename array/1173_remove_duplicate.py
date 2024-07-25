def removeDuplicate(nums):
    nums.sort()
    newNums = []

    for num in nums:
        if num not in newNums:
            newNums.append(num)
    
    nums[:] = newNums
    return nums

print(removeDuplicate([1,1,2]))