import numpy as np

# initial_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])       
# goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# i = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]

# print('Initial state:', initial_state)
# print('Goal state:', goal_state)
# print('i:', i)  

# /////////////////////////////////////////////////////////////////////////////

# def node_state(matrix):
#     # Using NumPy functions to find the indices where the value is 0
#     indices = np.where(matrix == 0)

#     # The result is a tuple of arrays, so extracting the values
#     i, j = indices[0][0], indices[1][0]

#     return i, j

# # Example usage:
# current_node = np.array([[1, 0, 3], [4, 2, 5], [6, 7, 8]])
# node_state = node_state(current_node)

# print("Location of the blank tile:", node_state)


# //////////////////////////////////////////////////////////////////////////


# def ActionMoveLeft(current_node):
#     i, j = find_blank_location(current_node)
#     if j > 0:
#         new_node = current_node.copy()
#         new_node[i, j], new_node[i, j-1] = new_node[i, j-1], new_node[i, j]
#         return True, new_node
#     else:
#         return False, None

# def ActionMoveRight(current_node):
#     i, j = find_blank_location(current_node)
#     if j < 2:
#         new_node = current_node.copy()
#         new_node[i, j], new_node[i, j+1] = new_node[i, j+1], new_node[i, j]
#         return True, new_node
#     else:
#         return False, None

# def ActionMoveUp(current_node):
#     i, j = find_blank_location(current_node)
#     if i > 0:
#         new_node = current_node.copy()
#         new_node[i, j], new_node[i-1, j] = new_node[i-1, j], new_node[i, j]
#         return True, new_node
#     else:
#         return False, None

# def ActionMoveDown(current_node):
#     i, j = find_blank_location(current_node)
#     if i < 2:
#         new_node = current_node.copy()
#         new_node[i, j], new_node[i+1, j] = new_node[i+1, j], new_node[i, j]
#         return True, new_node
#     else:
#         return False, None

# def find_blank_location(matrix):
#     indices = np.where(matrix == 0)
#     i, j = indices[0][0], indices[1][0]
#     return i, j

# # Example usage:
# current_node = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])



# status, new_node = ActionMoveLeft(current_node)
# print("Move Left Status:", status)
# if status:
#     print("New Node after Move Left:")
#     print(new_node)

# status, new_node = ActionMoveRight(current_node)
# print("\nMove Right Status:", status)
# if status:
#     print("New Node after Move Right:")
#     print(new_node)

# status, new_node = ActionMoveUp(current_node)
# print("\nMove Up Status:", status)
# if status:
#     print("New Node after Move Up:")
#     print(new_node)

# status, new_node = ActionMoveDown(current_node)
# print("\nMove Down Status:", status)
# if status:
#     print("New Node after Move Down:")
#     print(new_node)

# //////////////////////////////////////////////////////////////////////////

from collections import defaultdict
import numpy as np

class PuzzleGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_state, goal_state):
        visited = set()
        queue = []

        queue.append(start_state)
        visited.add(tuple(start_state.flatten()))

        while queue:
            current_state = queue.pop(0)
            print(current_state)  # Print or process the current state as needed

            if np.array_equal(current_state, goal_state):
                print("Goal state reached!")
                break

            for next_state in self.get_possible_moves(current_state):
                tuple_next_state = tuple(next_state.flatten())
                if tuple_next_state not in visited:
                    queue.append(next_state)
                    visited.add(tuple_next_state)

    def get_possible_moves(self, state):
        possible_moves = []

        # Move the blank tile left
        status, new_state = ActionMoveLeft(state, [])
        if status:
            possible_moves.append(new_state)

        # Move the blank tile right
        status, new_state = ActionMoveRight(state, [])
        if status:
            possible_moves.append(new_state)

        # Move the blank tile up
        status, new_state = ActionMoveUp(state, [])
        if status:
            possible_moves.append(new_state)

        # Move the blank tile down
        status, new_state = ActionMoveDown(state, [])
        if status:
            possible_moves.append(new_state)

        return possible_moves

def ActionMoveLeft(current_node, visited_nodes):
    i, j = find_blank_location(current_node)
    if j > 0:
        new_node = current_node.copy()
        new_node[i, j], new_node[i, j-1] = new_node[i, j-1], new_node[i, j]
        if not is_node_visited(new_node, visited_nodes):
            return True, new_node
    return False, None

def ActionMoveRight(current_node, visited_nodes):
    i, j = find_blank_location(current_node)
    if j < 2:
        new_node = current_node.copy()
        new_node[i, j], new_node[i, j+1] = new_node[i, j+1], new_node[i, j]
        if not is_node_visited(new_node, visited_nodes):
            return True, new_node
    return False, None

def ActionMoveUp(current_node, visited_nodes):
    i, j = find_blank_location(current_node)
    if i > 0:
        new_node = current_node.copy()
        new_node[i, j], new_node[i-1, j] = new_node[i-1, j], new_node[i, j]
        if not is_node_visited(new_node, visited_nodes):
            return True, new_node
    return False, None

def ActionMoveDown(current_node, visited_nodes):
    i, j = find_blank_location(current_node)
    if i < 2:
        new_node = current_node.copy()
        new_node[i, j], new_node[i+1, j] = new_node[i+1, j], new_node[i, j]
        if not is_node_visited(new_node, visited_nodes):
            return True, new_node
    return False, None

def find_blank_location(matrix):
    indices = np.where(matrix == 0)
    i, j = indices[0][0], indices[1][0]
    return i, j

def is_node_visited(node, visited_nodes):
    return any(np.array_equal(node, visited_node) for visited_node in visited_nodes)

if __name__ == '__main__': 
    start_state = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    puzzle_graph = PuzzleGraph()

    # Add edges based on possible moves from each state
    for i in range(3):
        for j in range(3):
            current_state = start_state.copy()
            status, new_state = ActionMoveLeft(current_state, [])
            if status:
                puzzle_graph.add_edge(tuple(current_state.flatten()), tuple(new_state.flatten()))

            status, new_state = ActionMoveRight(current_state, [])
            if status:
                puzzle_graph.add_edge(tuple(current_state.flatten()), tuple(new_state.flatten()))

            status, new_state = ActionMoveUp(current_state, [])
            if status:
                puzzle_graph.add_edge(tuple(current_state.flatten()), tuple(new_state.flatten()))

            status, new_state = ActionMoveDown(current_state, [])
            if status:
                puzzle_graph.add_edge(tuple(current_state.flatten()), tuple(new_state.flatten()))

    print("BFS Traversal of the 8-puzzle state space:")
    puzzle_graph.bfs(start_state, goal_state)


