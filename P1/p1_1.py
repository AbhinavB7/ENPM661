import numpy as np

initial_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])       
goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print('Initial state: \n', initial_state)
print('Goal state: \n', goal_state)

# /////////////////////////////////////////////////////////////////////////////

# location of the blank tile

def node_state(matrix):
    # Using NumPy functions to find the indices where the value is 0
    indices = np.where(matrix == 0)

    # The result is a tuple of arrays, so extracting the values
    i, j = indices[0][0], indices[1][0]

    print (f'({i},  {j})')
    return i, j

node_state(initial_state)
node_state(goal_state)

# //////////////////////////////////////////////////////////////////////////

# write 4 sub functions to move the blank tile in 4 directions

def ActionMoveLeft(current_node):
    i, j = node_state(current_node)
    if j > 0:
        new_node = current_node.copy()
        new_node[i, j], new_node[i, j-1] = new_node[i, j-1], new_node[i, j]
        return True, new_node
    else:
        return False, None

def ActionMoveRight(current_node):
    i, j = node_state(current_node)
    if j < 2:
        new_node = current_node.copy()
        new_node[i, j], new_node[i, j+1] = new_node[i, j+1], new_node[i, j]
        return True, new_node
    else:
        return False, None
    
def ActionMoveUp(current_node):
    i, j = node_state(current_node)
    if i > 0:
        new_node = current_node.copy()
        new_node[i, j], new_node[i-1, j] = new_node[i-1, j], new_node[i, j]
        return True, new_node
    else:
        return False, None
    
def ActionMoveDown(current_node):
    i, j = node_state(current_node)
    if i < 2:
        new_node = current_node.copy()
        new_node[i, j], new_node[i+1, j] = new_node[i+1, j], new_node[i, j]
        return True, new_node
    else:
        return False, None
    
# //////////////////////////////////////////////////////////////////////////

# append all the possible new nodes to the node_list

node_list = []
states_list = []
visited = []
not_visited = []

# //////////////////////////////////////////////////////////////////////////

# write a subfunction that uses backtracking to find the path from the initial state to the goal state

def find_path(node_list, goal):
    path = np.array([])
    current_node = node_list[-1]
    while not np.array_equal(current_node.state, initial_state):
        path = np.append(path, current_node.state)
        current_node = node_list[current_node.parent]
    return path

# //////////////////////////////////////////////////////////////////////////

# store all the info about node index, parent, and state in the NodesInfo.txt file

class Node:
    def __init__(self, node_id, parent, state):
        self.node_id = node_id
        self.parent = parent
        self.state = state
        
# store all the explored states in Nodes.txt file

def store_nodes(node_list):
    with open('Nodes.txt', 'w') as f:
        for node in node_list:
            f.write(f'{node.node_id} {node.parent} {node.state}\n')
            
# store the path from the initial state to the goal state in nodePath.txt file

# node index is the index of the current node in the node_list
# parent is the index of the parent node in the node_list
# state is the current state of the node





