def twoSum(nums, target):
    hashMap = {num: i for i, num in enumerate(nums)}

    for i in range(len(nums)):
        sub = target - nums[i];
        if sub not in nums: continue
        if hashMap[sub] != i:
            return [i, hashMap[sub]]
    return

# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([3, 3], 6))
print(twoSum([2,5,5,11], 10))
print(twoSum([1,3,4,2], 6))