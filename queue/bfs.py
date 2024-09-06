from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # List of neighboring nodes

def BFS(root, target):
    queue = deque([root])  # Initialize queue with the root node
    step = 0  # Number of steps needed from root to current node

    # BFS
    while queue:
        # Iterate over the current level
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()  # Get the first node in the queue
            if cur == target:  # Return the number of steps if cur is the target
                return step

            # Add all neighbors of the current node to the queue
            for next_node in cur.neighbors:
                queue.append(next_node)
        
        step += 1  # Increment the step count after processing a level

    return -1  # Return -1 if there is no path from root to target


# Example Nodes
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Create connections (undirected graph)
a.neighbors = [b, c]
b.neighbors = [a, d]
c.neighbors = [a]
d.neighbors = [b]

# BFS to find the shortest path from 'a' to 'd'
print(BFS(a, d))  # Output will be 2 (A -> B -> D)
