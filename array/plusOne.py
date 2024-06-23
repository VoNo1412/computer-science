## solution 1
def plusOne(nums):
    numStr = ""
    total = []
    for num in nums: numStr += str(num);
    for num in list(str(int(numStr) + 1)):
        total.append(int(num))
    

    return total


## solution 2
def plusOne2(digits):
    num = int("".join(map(str, digits))) + 1;
    return [int(digit) for digit in str(num)];

print(plusOne2([9]))
print(plusOne2([1,2,3]))
print(plusOne2([9, 9]))