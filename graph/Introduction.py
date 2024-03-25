# Two types of graph : Directed and Undirected

# degree of Undirected graph ---> 2 x Edges.
# degree of Directed graph ---------> Indegree
#                          |--------> Outdegree

# Edge weights -------> number asigned to edges.

# Representation of Graphs ---------> n nodes, m edges
# m lines or m pairs of nodes representing edges ----------> input of graph
# 2 ways to store ---> 1) Matrix (Adjacency Matrix)
#                      2) List

class Graph:

    def adjacency_matrix(self, n, m, edges):
        self.adj = [[0] * (n + 1) for _ in range(n + 1)]
        for edge in edges:
            u, v = edge
            self.adj[u][v] = 1
            self.adj[v][u] = 1

    def printAdj(self):
        print("Adjacency Matrix : ", end="\n")
        for row in self.adj:
            print(*row)
        print()

    def adjacency_list(self, n, m, edges):
        self.adjList = list([] for i in range(n+1))
        for i in edges:
            self.adjList[i[0]].append(i[1])
            self.adjList[i[1]].append(i[0])

    def printAdjList(self):
        print("Adjacency List:")
        for i, row in enumerate(self.adjList):
            print(f"{i}->", end=" ")
            print(*row)
        print()

if __name__ == "__main__":
    g = Graph()
    n = 5
    m = 6
    edges = [
        [1, 2],
        [1, 3],
        [3, 4],
        [2, 4],
        [2, 5],
        [4, 5]
    ]

    g.adjacency_matrix(n,m, edges)
    g.printAdj()

    g.adjacency_list(n, m, edges)
    g.printAdjList()

