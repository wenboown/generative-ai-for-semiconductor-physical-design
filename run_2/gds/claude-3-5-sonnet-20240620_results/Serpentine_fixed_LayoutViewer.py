import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define the parameters
path_width = 1  # 1 µm
num_turns = 15
segment_length = 50  # 50 µm
segment_height = 50  # 50 µm
layer = 2
datatype = 6

# Calculate the total number of points needed
num_points = 2 + 4 * num_turns

# Initialize the points array
points = np.zeros((num_points, 2))

# Generate the serpentine pattern points
for i in range(num_turns):
    base_index = 4 * i
    y_offset = i * segment_height
    
    if i % 2 == 0:
        # Even turn (left to right)
        points[base_index] = (0, y_offset)
        points[base_index + 1] = (segment_length, y_offset)
        points[base_index + 2] = (segment_length, y_offset + segment_height)
        points[base_index + 3] = (0, y_offset + segment_height)
    else:
        # Odd turn (right to left)
        points[base_index] = (segment_length, y_offset)
        points[base_index + 1] = (0, y_offset)
        points[base_index + 2] = (0, y_offset + segment_height)
        points[base_index + 3] = (segment_length, y_offset + segment_height)

# Add the last two points to close the path
points[-2] = points[-3]
points[-1] = points[0]

# Create the serpentine path
serpentine = gdspy.FlexPath(
    points,
    path_width,
    corners='circular bend',
    bend_radius=path_width/2,
    layer=layer,
    datatype=datatype
)

# Add the serpentine path to the cell
cell.add(serpentine)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

# Optional: View the layout