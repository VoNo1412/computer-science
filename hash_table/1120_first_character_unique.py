def firstUniqChar(s):
    char_count = {}

    # First pass: Count the occurrences of each character
    for i, v in enumerate(s):
        if v in char_count:
            char_count[v] += 1
        else:
            char_count[v] = 1

    print(char_count)
    # Second pass: Find the index of the first unique character
    for i, v in enumerate(s):
        if char_count[v] == 1:
            return i

    return -1
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))