def implementStr(haystack, needle):
    return haystack.find(needle) if haystack.find(needle) != -1 else -1



print(implementStr("sadbutsad", "sad"))
print(implementStr("leetcode", "leeto"))
print(implementStr("hello", "ll"))