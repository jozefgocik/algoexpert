# Solution 1
# def validIPAddresses(string):
#     # O(1) time / O(1) space;
#     result = []
#     validIPAddressesHelper(string, "", "", 0, len(string), result)
#     return result
#
#
# def validIPAddressesHelper(string, substring, address, dot, length, result):
#     if substring != "" and int(substring) > 255 or len(substring) > 1 and substring[0] == "0":
#         return
#     elif substring != "":
#         address += substring if dot == 4 else substring + "."
#
#     if dot == 4:
#         if len(address) == length + 3:
#             result.append(address)
#         return
#
#     if len(string) >= 1:
#         validIPAddressesHelper(string[1:len(string)], string[0], address, dot + 1, length, result)
#     if len(string) > 1:
#         validIPAddressesHelper(string[2:len(string)], string[0:2], address, dot + 1, length, result)
#     if len(string) > 2:
#         validIPAddressesHelper(string[3:len(string)], string[0:3], address, dot + 1, length, result)

# Solution 2
def validIPAddresses(string):
    # O(1) time / O(1) space
    result = []

    for i in range(1, min(len(string), 4)):
        currentIPAddress = ["", "", "", ""]

        currentIPAddress[0] = string[:i]
        if not isValidPart(currentIPAddress[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddress[1] = string[i:j]
            if not isValidPart(currentIPAddress[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddress[2] = string[j:k]
                currentIPAddress[3] = string[k:len(string)]
                if isValidPart(currentIPAddress[2]) and isValidPart(currentIPAddress[3]):
                    result.append(".".join(currentIPAddress))

    return result

def isValidPart(string):
    intAsString = int(string)
    if intAsString > 255:
        return False

    return len(string) == len(str(intAsString))

print(validIPAddresses("1921680"))
print(validIPAddresses("3700100"))
