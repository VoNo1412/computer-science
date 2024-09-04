def logngestSubstring(s):
    # abcabcbb

    last_seen = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
            print("before: ", start, last_seen[char])

        last_seen[char] = i
        max_length = max(max_length, i - start + 1)


    return max_length


print(logngestSubstring("abcabcbb"))
print(logngestSubstring("bbbbb"))
# print(logngestSubstring("pwwkew"))    
# print(logngestSubstring("au"))    
# print(logngestSubstring(" "))    
# print(logngestSubstring("aab"))    
# print(logngestSubstring("cdd"))    
# print(logngestSubstring("dvdf"))    