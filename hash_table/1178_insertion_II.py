def insertionII(nums1, nums2):
    char_numI = {}
    char_numII = {}

    for nums in nums1:
        if nums in char_numI:
            char_numI[nums] += 1
        else:
            char_numI[nums] = 1

    for nums in nums2:
        if nums in char_numII:
            char_numII[nums] += 1
        else:
            char_numII[nums] = 1
    
    intersection = []
    # Find intersection
    for num in char_numI:
        if num in char_numII:
            # The count for intersection is the minimum of the two counts
            intersection.extend([num] * min(char_numI[num], char_numII[num]))

    return intersection
        



print(insertionII([1,2,2,1], [2, 2]))
print(insertionII([4,9,5], [9,4,9,8,4]))
print(insertionII([1, 2], [1, 1]))
print(insertionII([1,2,2,1], [2]))
print(insertionII([3,1,2], [1, 1]))
