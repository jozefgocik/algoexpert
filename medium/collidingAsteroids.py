def collidingAsteroids(asteroids):
    # O(n) time / O(n) space
    stack = []

    for i in range(len(asteroids)):
        collidingAsteroidsHelper(stack, asteroids[i])

    return stack

def collidingAsteroidsHelper(stack, asteroid):
    if not stack:
        stack.append(asteroid)
    elif stack[-1] > 0 and asteroid < 0:
        if abs(stack[-1]) > abs(asteroid):
            return
        if abs(stack[-1]) < abs(asteroid):
            stack.pop()
            collidingAsteroidsHelper(stack, asteroid)
        else:
            stack.pop()
    else:
        stack.append(asteroid)

print(collidingAsteroids([-3, 5, -8, 6, 7, -4, -7]))