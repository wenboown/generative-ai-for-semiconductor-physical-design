import gdspy
import numpy as np

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OVAL')

# Define oval parameters
major_axis = 20000  # 20 mm in nanometers
minor_axis = 13000  # 13 mm in nanometers
num_points = 200  # Number of points to approximate the oval

# Generate points for the oval
t = np.linspace(0, 2*np.pi, num_points)
x = (major_axis/2) * np.cos(t)
y = (minor_axis/2) * np.sin(t)

# Create the oval polygon
oval = gdspy.Polygon(np.column_stack((x, y)), layer=0)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been generated.")