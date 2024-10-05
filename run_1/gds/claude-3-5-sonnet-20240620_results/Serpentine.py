import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define the parameters
path_width = 1  # µm
num_turns = 15
segment_length = 50  # µm
layer = 2
datatype = 6

# Calculate the total number of segments
total_segments = num_turns * 2 + 1

# Create a list to store the points of the serpentine pattern
points = [(0, 0)]

# Generate the points for the serpentine pattern
for i in range(1, total_segments):
    x, y = points[-1]
    if i % 2 == 1:
        # Horizontal segment
        x += segment_length if i % 4 == 1 else -segment_length
    else:
        # Vertical segment
        y += segment_length
    points.append((x, y))

# Create the serpentine pattern using PathPolygon
serpentine = gdspy.PathPolygon(points, path_width, layer=layer, datatype=datatype)

# Add the serpentine pattern to the cell
cell.add(serpentine)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

print("Serpentine pattern has been generated and saved to 'serpentine_pattern.gds'.")