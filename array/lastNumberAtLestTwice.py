## Solve problem 1

def dominantIndex(nums):
    maxNumber = index = - 1;

    ## find max number
    for i, num in enumerate(nums): 
        if maxNumber < num: 
            maxNumber = num; 
            index = i;

    # check least twice
    for i, num in enumerate(nums):
        if num * 2 > maxNumber and num != maxNumber: return -1;

    return index



## Solve problem 2
def dominantIndex2(nums):
    hashMap = {num: i for i, num in enumerate(nums)}
    maxNumber = max(nums);
    
    for num in nums:
        if num * 2 > maxNumber and maxNumber != num: return -1;

    return hashMap[maxNumber];


print(dominantIndex2([3,6,1,0]))
print(dominantIndex2([1,2,3,4]))