import sys

class Node:
    def __init__(self, nodeId):
        self.id = nodeId
        self.neighbors = []
        
    def addNeighbor(self, n):
        self.neighbors.append(n)
    
    def __str__(self):
        return 'Node %d %s' % (self.id, self.neighbors)
    
    def __repr__(self):
        return self.__str__()

nodes = {}

def getNode(n):
    node = nodes.get(n, None)
    if node is None:
        node = Node(n)
        nodes[n] = node
    return node

def getKey(id1, id2):
    if id1 >= id2:
        return '%d-%d' % (id2, id1)
    else:
        return '%d-%d' % (id1, id2)

costs = {}

def prune(root):
    nodesList = [root]
    seenNodes = []
    
    minCost = None
    minEdge = None 
    
    while len(nodesList) > 0:
        node = getNode(nodesList.pop(0))
        
        # keep seen nodes
        seenNodes.append(node.id)
        
        # if lonely node, remove and skip it
        if len(node.neighbors) == 0:
            nodes.pop(node.id)
        # if leaf and not infected, remove it
        elif len(node.neighbors) == 1 and node.id not in machines:
            nodes.pop(node.id)
            neighbor = getNode(node.neighbors[0])
            neighbor.neighbors.remove(node.id)
            edge = getKey(node.id, neighbor.id)
            costs.pop(edge)
            nodesList.append(neighbor.id)
        else:
            for n in node.neighbors:
                # don't consider same node twice
                if n in seenNodes:
                    continue
                
                neighbor = getNode(n)
                edge = getKey(node.id, n)
                
                # remove leaves that have no machines
                if len(neighbor.neighbors) == 1 and n not in machines:
                    # delete node
                    node.neighbors.remove(n)
                    nodes.pop(n)
                    # also delete edge
                    costs.pop(edge)
                elif (len(neighbor.neighbors) > 1 or n in machines) and n not in nodesList:
                    nodesList.append(n)
                    # keep min cost edge
                    cost = costs[edge]
                    if minCost is None or cost < minCost:
                        minCost = cost
                        minEdge = edge
    
    return minCost, minEdge 
                

# read N and K
firstLine = sys.stdin.readline().strip().split(' ')
N = int(firstLine[0])
K = int(firstLine[1])

roots = []
    
# read graph
for i in range(N - 1):
    line = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    node1 = getNode(line[0])
    node2 = getNode(line[1])
    
    node1.addNeighbor(node2.id)
    node2.addNeighbor(node1.id)
    
    if (len(roots) == 0):
        roots.append(node1.id)
    
    key = getKey(node1.id, node2.id)
    if (node2.id < node1.id):
        key = '%d-%d' % (node2.id, node1.id)
    costs[key] = line[2]
    
machines = []
# read machines
for i in range(K):
    line = sys.stdin.readline().strip()
    machines.append(int(line))
    
cost = 0
while len(roots) > 0:
    # pick root
    root = roots.pop(0)
    
    # prune tree to remove subtrees that do not contain a machine
    minCost, minEdge = prune(root)
    
    # was this subtree empty
    if minCost is not None:
        # add cost of chosen edge
        cost += minCost
        
        newRoots = [int(x) for x in minEdge.split('-')]
        
        # remove cheapest edge
        getNode(newRoots[0]).neighbors.remove(newRoots[1])
        getNode(newRoots[1]).neighbors.remove(newRoots[0])
        costs.pop(minEdge)
        
        # add new roots
        roots.extend(newRoots)
    
print(cost)