def fourSumII(A, B, C, D):
    hashSum = {}

    for a in A:
        for b in B:
            hashSum[a + b] = hashSum.get(a + b, 0) + 1

    print("hashSUm: ", hashSum)
    count= 0
    for c in C:
        for d in D:
            count += hashSum.get(-(c + d), 0) 
    return count


print(fourSumII([1,2], [-2,-1], [-1,2], [0,2]))