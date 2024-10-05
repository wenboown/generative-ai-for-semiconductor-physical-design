import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define the parameters
width = 1  # 1 µm width
segment_length = 50  # 50 µm segment length
num_turns = 15
layer = 2
datatype = 6

# Create the serpentine pattern
points = [(0, 0)]  # Start at (0, 0)
for i in range(num_turns):
    x, y = points[-1]
    if i % 2 == 0:
        # Even turns: go right then up
        points.append((x + segment_length, y))
        points.append((x + segment_length, y + segment_length))
    else:
        # Odd turns: go left then up
        points.append((x - segment_length, y))
        points.append((x - segment_length, y + segment_length))

# Create the path
path = gdspy.FlexPath(
    points,
    width,
    layer=layer,
    datatype=datatype,
    corners='round'
)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

# Optional: View the layout