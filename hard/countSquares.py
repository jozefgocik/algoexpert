def countSquares(points):
    # O(n ^ 2) time / O(n) space
    result = 0
    pointsSet = set(pointToString(i) for i in points)

    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midpoint = [(pointA[0] + pointB[0])/2, (pointA[1] + pointB[1])/2]
            xDistance = pointA[0] - midpoint[0]
            yDistance = pointA[1] - midpoint[1]

            pointC = [midpoint[0] + yDistance, midpoint[1] - xDistance]
            pointD = [midpoint[0] - yDistance, midpoint[1] + xDistance]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                result += 1

    return result/4

def pointToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(i) for i in point]

    return ",".join([str(i) for i in point])


print(countSquares([
    [1, 1],
    [0, 0],
    [-4, 2],
    [-2, -1],
    [0, 1],
    [1, 0],
    [-1, 4]
]))