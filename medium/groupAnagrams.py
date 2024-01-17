def groupAnagrams(words):
    # O(n * l * log(n)) / O(n * l) space; n = number of words, l = length of the longest word
    groups = {}

    for i in range(len(words)):
        sortedWord = sorted(words[i])
        word = "".join(sortedWord)
        if word not in groups:
            groups[word] = [words[i]]
        else:
            groups[word].append(words[i])

    return [value for value in groups.values()]

print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))