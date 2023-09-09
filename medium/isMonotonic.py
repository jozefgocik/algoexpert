def isMonotonic(array):
    # O(n) time / O(1) space
    state = 0  # -1 = non-decreasing, 0 = default, 1 = non-increasing

    if len(array) == 1:
        return True

    for i in range(0, len(array) - 1):
        if array[i] == array[i+1]:
            continue
        elif array[i] < array[i+1] and state != 1:
            state = -1
        elif array[i] > array[i+1] and state != -1:
            state = 1
        else:
            return False

    return True

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# true