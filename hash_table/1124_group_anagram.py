def groupAnagram(strs):
    d = {}

    for str in strs:
        letterSorted = "".join(sorted(str))
        if letterSorted not in d:
            d[letterSorted] = []
        d[letterSorted].append(str)
        
    return list(sorted(d.values()))
    



print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))