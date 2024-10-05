import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OVAL')

# Define the oval parameters
major_axis = 20000  # 20 mm in nanometers
minor_axis = 13000  # 13 mm in nanometers
center = (0, 0)
layer = 0

# Create the oval
# We'll use a polygon approximation with 64 points for smoothness
t = np.linspace(0, 2*np.pi, 64)
x = center[0] + major_axis/2 * np.cos(t)
y = center[1] + minor_axis/2 * np.sin(t)
oval = gdspy.Polygon(np.column_stack((x, y)), layer=layer)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been created successfully.")