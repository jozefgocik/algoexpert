def commonCharacters(strings):
    # Write your code here.
    result = []
    for i in strings[0]:
        if i not in result:
            result.append(i)

    for i in range(1, len(strings)):
        for j in result:
            if j not in strings[i]:
                result.remove(j)

    return result


print(commonCharacters(["abc", "bcd", "cbad"]))