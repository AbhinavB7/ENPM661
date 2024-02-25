import numpy as np

class Node:
    def __init__(self, node_id, parent, state):
        self.node_id = node_id
        self.parent = parent
        self.state = state
        
initial_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])       
goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# print('Initial state: \n', initial_state)
# print('Goal state: \n', goal_state)


# /////////////////////////////////////////////////////////////////////////////

# location of the blank tile

def node_state(matrix):
    indices = np.where(matrix == 0)
    i, j = indices[0][0], indices[1][0]
    return i, j

# node_state(initial_state)
# node_state(goal_state)

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
    path = []
    current_node = node_list[-1]
    while not np.array_equal(current_node.state, initial_state):
        path.append(current_node.state.tolist())
        current_node = node_list[current_node.parent]
    path.reverse()
    return path

# //////////////////////////////////////////////////////////////////////////

def bfs(initial_state, goal_state):
    node_list = []
    states_list = []
    visited = []
    not_visited = []
    node_list.append(Node(0, -1, initial_state))
    states_list.append(tuple(map(tuple, initial_state)))
    not_visited.append(0)
    node_id = 0
    while not_visited:
        current_node = not_visited.pop(0)
        visited.append(current_node)
        if np.array_equal(node_list[current_node].state, goal_state):
            print('Goal state found')
            store_nodes(node_list)
            store_nodes_info(node_list)
            store_path(node_list)
            return node_list
        else:
            left, new_node = ActionMoveLeft(node_list[current_node].state)
            if left:
                new_node_tuple = tuple(map(tuple, new_node))
                if new_node_tuple not in states_list:
                    node_id += 1
                    node_list.append(Node(node_id, current_node, new_node))
                    states_list.append(new_node_tuple)
                    not_visited.append(node_id)
            right, new_node = ActionMoveRight(node_list[current_node].state)
            if right:
                new_node_tuple = tuple(map(tuple, new_node))
                if new_node_tuple not in states_list:
                    node_id += 1
                    node_list.append(Node(node_id, current_node, new_node))
                    states_list.append(new_node_tuple)
                    not_visited.append(node_id)
            up, new_node = ActionMoveUp(node_list[current_node].state)
            if up:
                new_node_tuple = tuple(map(tuple, new_node))
                if new_node_tuple not in states_list:
                    node_id += 1
                    node_list.append(Node(node_id, current_node, new_node))
                    states_list.append(new_node_tuple)
                    not_visited.append(node_id)
            down, new_node = ActionMoveDown(node_list[current_node].state)
            if down:
                new_node_tuple = tuple(map(tuple, new_node))
                if new_node_tuple not in states_list:
                    node_id += 1
                    node_list.append(Node(node_id, current_node, new_node))
                    states_list.append(new_node_tuple)
                    not_visited.append(node_id)

    return None

# //////////////////////////////////////////////////////////////////////////
  
# store all the info about node index, parent, and state in the NodesInfo.txt file


# store all the explored states in a list to Nodes.txt file

def store_nodes(node_list):
    with open('Nodes.txt', 'w') as f:
        for node in node_list:
            f.write(f'{node.state}\n')
            
# store all the information about the node index, parent node index, and node in NodesInfo.txt file

def store_nodes_info(node_list):
    with open('NodesInfo.txt', 'w') as f:
        for node in node_list:
            f.write(f'{node.node_id} {node.parent} {node.state}\n')

# store the order of the states from start node to the goal node in nodePath.txt file

def store_path(node_list):
    with open('nodePath.txt', 'w') as f:
        path = find_path(node_list, goal_state)
        for node in path:
            f.write(f'{node}\n')
            
            
# node index is the index of the current node in the node_list
# parent is the index of the parent node in the node_list
# state is the current state of the node


# //////////////////////////////////////////////////////////////////////////


def main():
    
    # initial_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
    # init_mat = np.array([[4, 7, 0], [1, 2, 8], [3, 5, 6]])  # Test case 1
    initial_state = np.array([[1, 4, 7], [2, 5, 8], [3, 0, 6]])  # Test case 2
    # init_mat = np.array([[4, 5, 8], [2, 1, 7], [3, 6, 0]])  # Test case 3
    goal_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])

    print('Initial state: \n', initial_state)
    
    node_list = bfs(initial_state, goal_state)

    if node_list:
        # Print each step
        for step, node in enumerate(node_list):
            print(f'Step {step}:\n{np.array(node.state)}\n')
    print('Goal state: \n', goal_state)
    
if __name__ == '__main__':
    main()
  


