def isomorphic(s, t):
    hashSMap = {}
    hashTMap = {}

    for i in range(len(t)):
        if s[i] in hashSMap and hashSMap[s[i]] != t[i]:
            return False
        if t[i] in hashTMap and hashTMap[t[i]] != s[i]:
            return False
        hashTMap[t[i]] = s[i]
        hashSMap[s[i]] = t[i]
    return True

print(isomorphic("egg", "add"))
print(isomorphic("foo", "bar"))
print(isomorphic("paper", "title"))
print(isomorphic("badc", "baba"))