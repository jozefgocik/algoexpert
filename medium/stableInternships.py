def stableInternships(interns, teams):
    # O(n^2) time / O(n^2) space
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)

    teamMaps = []
    for team in teams:
        rank = {}
        for i, internNumber in enumerate(team):
            rank[internNumber] = i
        teamMaps.append(rank)

    while len(freeInterns) > 0:
        internNumber = freeInterns.pop()

        intern = interns[internNumber]
        teamPreference = intern[currentInternChoices[internNumber]]
        currentInternChoices[internNumber] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = internNumber
            continue

        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNumber]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            chosenInterns[teamPreference] = internNumber
        else:
            freeInterns.append(internNumber)

    matches = [[internNum, teamNum] for teamNum, internNum in chosenInterns.items()]

    return matches

print(stableInternships(
    interns=[
        [0, 1, 2],
        [1, 0, 2],
        [1, 2, 0]
    ],
    teams=[
        [2, 1, 0],
        [1, 2, 0],
        [0, 2, 1]
    ]
))