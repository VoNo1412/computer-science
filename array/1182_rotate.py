def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]



print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([1,2], 3))