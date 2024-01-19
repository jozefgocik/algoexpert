def minimumCharactersForWords(words):
    # O(n * l) time / O(c) space; n = number of words, l = length of longest word, c = number of unique chars
    result = []
    chars = {}

    for i in range(len(words)):
        currentChars = {}
        for char in words[i]:
            if char not in currentChars:
                currentChars[char] = 0
            currentChars[char] += 1

        for key, value in currentChars.items():
            if key not in chars:
                chars[key] = value
            else:
                chars[key] = max(chars[key], value)

    for key, value in chars.items():
        for _ in range(value):
            result.append(key)

    return result

print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))