def removeElement(nums, target):
    k = 0
    for x in nums:
        if x != target:
            nums[k] = x
            k += 1

    return k

removeElement([3, 2, 2, 3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)