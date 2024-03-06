# Importing the necessary libraries
import numpy as np
import cv2
import math
# from google.colab.patches import cv2_imshow

# Defining the clearance (clearance = 5)
clr = 5

# Defining the size of canvas
width, height = 1200, 500

# Defining different colors to illustrate obstacles
cyan = [185, 0, 2]
blue = [255, 125, 0]

# Writing function to display the obstacles and clearance on the canvas
def Obstacles(obs):
    center = (650, 250)
    hexagon_side_length = 150
    y = 500

    hexagon_vertices = []
    for i in range(6):
        angle_rad = math.radians(30 + 60 * i)  # 60 degrees between each vertex
        hexagon_x = int(center[0] + hexagon_side_length * math.cos(angle_rad))
        hexagon_y = int(center[1] + hexagon_side_length * math.sin(angle_rad))
        hexagon_vertices.append((hexagon_x, hexagon_y))

    # Fill the larger hexagon
    cv2.fillPoly(obs, [np.array(hexagon_vertices)], blue)

    # Smaller hexagon inside with clearance
    hexagon_side_length1 = 140
    hexagon_vertices1 = [(int(center[0] + hexagon_side_length1 * math.cos(math.radians(30 + 60 * i))),
                          int(center[1] + hexagon_side_length1 * math.sin(math.radians(30 + 60 * i))))
                         for i in range(6)]

    # Fill the smaller hexagon
    cv2.fillPoly(obs, [np.array(hexagon_vertices1)], cyan)

    rect_inside = [
        ((100 - clr, y - 100 + clr), (175 + clr, y - height)),
        ((275 - clr, y - 0), (350 + clr, y - 400 - clr)),
        ((980 - clr, y - 50 + clr), (1055 + clr, y - 450 - clr)),
        ((850 - clr, y - 50 + clr), (1055 + clr, y - 125 - clr)),
        ((850 - clr, y - 375 + clr), (1055 + clr, y - 450 - clr))
    ]

    rect_outside = [
        ((100, y - 100), (175, y - height)),
        ((275, y - 0), (350, y - 400)),
        ((980, y - 50), (1055, y - 450)),
        ((850, y - 50), (1055, y - 125)),
        ((850, y - 375), (1055, y - 450))
    ]

    for rect in rect_inside:
        cv2.rectangle(obs, rect[0], rect[1], blue, thickness=-1)
    
    for rect in rect_outside:
        cv2.rectangle(obs, rect[0], rect[1], cyan, thickness=-1)
    
    # Defining clearance on the borders
    obs[:clr, :] = blue  # top
    obs[-clr:, :] = blue  # bottom
    obs[:, :clr] = blue  # left
    obs[:, -clr:] = blue  # right

    return obs

# Initialize canvas
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Call Obstacles function to populate the canvas
obstacle_map = Obstacles(canvas.copy())

# Display the map
# cv2_imshow(obstacle_map)


# //////////////////////////////////////////////////////////////////////

# Inital and Goal Nodes 

while True:
  start_x = int(input("Enter start point, x (6-1195): "))
  start_y = int(input("Enter start point, y (6-495): "))
  start_node = [start_x, start_y]

  if start_node[0] < 6 or start_node[0] >= width or start_node[1] < 6 or start_node[1] >= height:
      print("Out of canvas!!! Provide new coordinates!!")
  elif ((obstacle_map[499 - start_node[1], start_node[0]])).all() or ((obstacle_map[499 - start_node[1], start_node[0]]) == cyan).all():
      print("Obstacle !!! Provide new coordinates!!")
  else:
      break

while True:
  goal_x = int(input("Enter end point, x (6-1195): "))
  goal_y = int(input("Enter end point, y (6-495): "))
  goal_node = [goal_x, goal_y]

  if goal_node[0] < 6 or goal_node[0] >= width or goal_node[1] < 6 or goal_node[1] >= height:
      print("Out of canvas!!! Provide new coordinates!!")
  elif ((obstacle_map[499 - goal_node[1], goal_node[0]])).all() or ((obstacle_map[499 - goal_node[1], goal_node[0]]) == cyan).all():
      print("Obstacle !!! Provide new coordinates!!")
  else:
      break
  
  
  # //////////////////////////////////////////////////////////////////////