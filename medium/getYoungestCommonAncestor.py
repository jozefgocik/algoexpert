# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Solution 1
# def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
#     # O(d) time / O(d) space; d = depth of the ancestral tree
#     if descendantOne == topAncestor or descendantTwo == topAncestor:
#         return topAncestor
#
#     potentialAncestor = descendantOne
#     while potentialAncestor is not None:
#         ancestor = getYoungestCommonAncestorHelper(potentialAncestor, descendantTwo)
#         if ancestor is not None:
#             return ancestor
#
#         potentialAncestor = potentialAncestor.ancestor
#
# def getYoungestCommonAncestorHelper(potentialAncestor, descendantTwo):
#     if descendantTwo == potentialAncestor:
#         return potentialAncestor
#     if descendantTwo.ancestor is None:
#         return None
#
#     return getYoungestCommonAncestorHelper(potentialAncestor, descendantTwo.ancestor)


# Solution 2
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # O(d) time / O(1) space; d = depth of the ancestral tree
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor, descendantTwo)

    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def backtrackAncestralTree(lowerDescendant, higherDescendant, difference):
    while difference > 0:
        lowerDescendant = lowerDescendant.ancestor
        difference -= 1

    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor

    return lowerDescendant

def getDescendantDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor

    return depth