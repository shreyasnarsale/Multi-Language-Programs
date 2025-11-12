# Graph Traversal using BFS and DFS

# Locations (Nodes): A, B, C, D, E

# Representing graph using Adjacency Matrix (for DFS)
adj_matrix = [
    [0, 1, 1, 0, 0],  # A connected to B, C
    [1, 0, 1, 1, 0],  # B connected to A, C, D
    [1, 1, 0, 0, 1],  # C connected to A, B, E
    [0, 1, 0, 0, 1],  # D connected to B, E
    [0, 0, 1, 1, 0]   # E connected to C, D
]

nodes = ['A', 'B', 'C', 'D', 'E']


# Depth First Search using Adjacency Matrix
def dfs(start):
    visited = [False] * len(nodes)
    stack = [start]
    print("DFS Traversal:", end=" ")

    while stack:
        current = stack.pop()
        if not visited[current]:
            print(nodes[current], end=" ")
            visited[current] = True
            # Push neighbors in reverse order to maintain correct order
            for i in range(len(nodes) - 1, -1, -1):
                if adj_matrix[current][i] == 1 and not visited[i]:
                    stack.append(i)
    print()


# Representing graph using Adjacency List (for BFS)
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}


# Breadth First Search using Adjacency List
from collections import deque

def bfs(start_node):
    visited = set()
    queue = deque([start_node])

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()


# --- Main Program ---
print("Graph Traversal starting from A:\n")
dfs(0)       # passing index of A for DFS
bfs('A')     # passing node name of A for BFS
