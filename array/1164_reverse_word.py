def reverse_word(s):
    a = [e for e in s.split(" ") if len(e) > 0]

    i = 0
    j = len(a) - 1

    while i < j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

        i += 1
        j -= 1
    s = " ".join(a)

    return s

print(reverse_word(" the sky               is blue "))