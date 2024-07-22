def twoSum(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i + 1, j + 1]
        elif (nums[i] + nums[j] > target):
            j -= 1
        else:
            i += 1

    return None

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1, 0], -1))