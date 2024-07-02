def addBinary(a, b):
    res = "";
    i = len(a) - 1;
    j = len(b) - 1;
    carry = 0;

    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        
        res = str(sum % 2) + res
        carry = sum // 2
      
    if carry > 0:
        res = "1" + res


    return res;



print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("111", "111"))