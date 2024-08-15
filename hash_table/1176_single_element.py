def singleNumber(nums):
    hashSet = set()

    for num in nums:
        if num not in hashSet:
            hashSet.add(num)
        else:
            hashSet.remove(num)
    
    return list(hashSet)[0]
    

print(singleNumber([1, 2, 2]))