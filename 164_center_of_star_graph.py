# Find Center of Star Graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = []
        
        n = len(edges[0])
        for i in range(n):
            result.append(edges[0][i])
        
        for i in range(len(result)):
            if result[i] in edges[1]:
        
                return result[i]
