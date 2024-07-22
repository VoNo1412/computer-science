def findMaxConsecutiveOnes( nums):
    k = temp = 0

    for num in nums:
        if num == 1:
            k += 1
            if k > temp:
                temp = k
        else:
            if k > temp:
                temp = k
            k = 0
            
    return temp

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
