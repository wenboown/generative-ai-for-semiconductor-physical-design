import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define the parameters
path_width = 1  # 1 µm
segment_length = 50  # 50 µm
segment_height = 50  # 50 µm
num_turns = 15
layer = 2
datatype = 6

# Create the list of points for the serpentine pattern
points = [(0, 0)]  # Starting point
for i in range(num_turns):
    x = points[-1][0]
    y = points[-1][1]
    
    if i % 2 == 0:  # Even turns go up and right
        points.append((x, y + segment_height))
        points.append((x + segment_length, y + segment_height))
    else:  # Odd turns go down and right
        points.append((x, y - segment_height))
        points.append((x + segment_length, y - segment_height))

# Create the path using FlexPath
path = gdspy.FlexPath(
    points,
    path_width,
    layer=layer,
    datatype=datatype,
    corners='natural'
)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

print("Serpentine pattern has been generated and saved to 'serpentine_pattern.gds'.")