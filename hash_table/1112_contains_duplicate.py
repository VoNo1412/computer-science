def findContainsDuplicate(nums):
    hashSet = set(nums)
    
    for num in nums:
        if num in hashSet:
            return True  # Duplicate found
        # hashSet.add(num)
    
    return False  # No duplicates found


print(findContainsDuplicate([1, 2, 3, 3]))
print(findContainsDuplicate([1, 2, 3, 4]))
print(findContainsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(findContainsDuplicate([1, 1]))
print(findContainsDuplicate([3, 3]))
        

