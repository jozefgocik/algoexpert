def topologicalSort(jobs, deps):
    # O(j + d) time / O(j + d) space; j = number of jobs, d = number of deps
    jobGraph = createJobGraph(jobs, deps)

    return getOrderOfJobs(jobGraph)


def getOrderOfJobs(graph):
    orderedJobs = []
    nodes = graph.nodes

    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []

    return orderedJobs


def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True

    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
        if containsCycle:
            return True

    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)

    for prereq, job in deps:
        # adding edges
        graph.addPrereq(job, prereq)

    return graph


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}

        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)

        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


# [1, 4, 3, 2] or [4, 1, 3, 2]
print(
    topologicalSort(
[1, 2, 3, 4],
[
      [1, 2],
      [1, 3],
      [3, 2],
      [4, 2],
      [4, 3]
    ]
    )
)