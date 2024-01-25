# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # O(n ^ 2) time / O(n ^ 2) space; n = length of string
        for i in range(len(string)):
            current = self.root
            for j in range(i, len(string)):
                if string[j] not in current:
                    current[string[j]] = {}
                current = current[string[j]]
            current[self.endSymbol] = True

    def contains(self, string):
        # O(n) time / O(1) space; n = length of string
        current = self.root
        for char in string:
            if char not in current:
                return False
            current = current[char]

        return self.endSymbol in current


print(SuffixTrie("babc").root)
