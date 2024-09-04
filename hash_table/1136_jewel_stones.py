def numJewelsInStones(jewels, stones):
    hashMap = {}

    for stone in stones:
        if stone in hashMap:
            hashMap[stone] += 1
        else:
            hashMap[stone] = 1
    
    count = 0
    for jewel in jewels:
        if jewel in hashMap:
            count += hashMap[jewel]

    return count;

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))

