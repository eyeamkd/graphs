# Implementation of Disjoint Set Union in Python 

# Given a set of nodes, implement the find() and the union() method 
# find() method should be able to find the node in the graph 
# union() method should be able to join the nodes 

class Node:
    value : int


class DSU:

    def __init__(self) -> None:
        self.graph = collections.defaultdict(list)

    def find(self, node: Node):
        # finds the root of a given vertex
        while self.graph[node.value]!=[]:
            node.value = self.graph[node.value]
        return node.value

    
    def union(self, from_node: Node, to_node: Node):
        self.graph[from_node.value].append(to_node.value)
        return 


