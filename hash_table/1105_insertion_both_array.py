def intersectionArray1(nums1, nums2):
    hashSet1 = set(nums1)
    hashSet2 = set(nums2)

    newArr = []
    for el in hashSet1:
        if el in hashSet2:
            newArr.append(el)

    return newArr

    

    
intersectionArray([1, 2, 2, 1], [2, 2])
intersectionArray([4,9,5], [9,4,9,8,4])
intersectionArray([3], [1])