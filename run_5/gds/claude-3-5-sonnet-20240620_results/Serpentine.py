import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define parameters
path_width = 1  # 1 µm
segment_length = 50  # 50 µm
num_turns = 15
layer = 2
datatype = 6

# Calculate the total number of points needed
num_points = 2 * num_turns + 2

# Create an array to hold the points
points = np.zeros((num_points, 2))

# Generate the points for the serpentine pattern
for i in range(num_points):
    x = (i // 2) * segment_length
    y = (i % 2) * segment_length
    points[i] = [x, y]

# Create the path
path = gdspy.FlexPath(
    points,
    path_width,
    layer=layer,
    datatype=datatype,
    corners='round'
)

# Add the path to the cell
cell.add(path)

# Save the library to a GDS file
lib.write_gds('serpentine_pattern.gds')

print("GDS file 'serpentine_pattern.gds' has been generated.")