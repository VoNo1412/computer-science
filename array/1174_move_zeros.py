def moveZero(nums):
    i, j = 0, 1

    while j < len(nums):
        if nums[i] == 0:
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1 
        else:
            i += 1
        j += 1

    print(nums)
    return nums; 


# print(moveZero([0,1,0,3,12])) # 
moveZero([0,1,0,3,12])
# [1, 0, 0, 3, 12]
# [1, 3, 0, 0, 12]
# [1, 3, 12, 0, 0]
# print(moveZero([1, 2]))
# print(moveZero([0, 1]))
# print(moveZero([1, 2, 3, 1]))
# print(moveZero([1, 2, 3, 1]))
print(moveZero([4,2,4,0,0,3,0,5,1,0])) ## [4,2,4,3,5,1,0,0,0,0]