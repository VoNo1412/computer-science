def reverse_letter(s):
    words = s.split()
    reverse_words = []
    for word in words:
        reverse_word = word[::-1]
        reverse_words.append(reverse_word)
    return " ".join(reverse_words)



print(reverse_letter("Let's take LeetCode contest"))
