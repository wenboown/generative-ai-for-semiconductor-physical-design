import numpy as np
import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('parametric_spiral')

# Define the parameters
t = np.linspace(0, 6 * np.pi, 1000)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the spiral path using FlexPath
spiral_path = gdspy.FlexPath(
    np.column_stack((x, y)),  # Points of the path
    width=1,                  # Line width
    layer=0,                  # Layer in GDS
    datatype=0                # Data type
)

# Add the path to the cell
cell.add(spiral_path)

# Save the GDS file
lib.write_gds('parametric_spiral.gds')

print("GDS file 'parametric_spiral.gds' has been created.")