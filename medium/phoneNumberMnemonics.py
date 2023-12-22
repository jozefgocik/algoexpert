def phoneNumberMnemonics(phoneNumber):
    # O(4^n * n) time / O(4^n * n) space
    mnemonics = []
    currentMnemonic = ["0"] * len(phoneNumber)
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonics)
    return mnemonics

def phoneNumberMnemonicsHelper(index, phoneNumber, currentMnemonic, mnemonics):
    if index == len(phoneNumber):
        mnemonics.append("".join(currentMnemonic))  # O(n)
    else:
        currentMnemonics = MNEMONICS[phoneNumber[index]]
        for i in range(0, len(currentMnemonics)):
            currentMnemonic[index] = currentMnemonics[i]
            phoneNumberMnemonicsHelper(index + 1, phoneNumber, currentMnemonic, mnemonics)


MNEMONICS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

print(phoneNumberMnemonics("1905"))