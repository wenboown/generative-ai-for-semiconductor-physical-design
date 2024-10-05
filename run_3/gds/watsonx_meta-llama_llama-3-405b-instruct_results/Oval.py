import gdspy
import numpy as np

# Define the GDS library and cell
gdspy.current_library = gdspy.GdsLibrary()
cell = gdspy.Cell('oval')

# Define the layer
layer = 0

# Define the oval parameters
major_axis = 20  # mm
minor_axis = 13  # mm
center = (0, 0)  # mm

# Create an array of angles from 0 to 2π
angles = np.linspace(0, 2*np.pi, 100)

# Calculate the x and y coordinates of the oval
x = center[0] + major_axis/2 * np.cos(angles)
y = center[1] + minor_axis/2 * np.sin(angles)

# Create a polygon from the coordinates
polygon = gdspy.Polygon([(x[i], y[i]) for i in range(len(x))], layer=layer)

# Add the polygon to the cell
cell.add(polygon)

# Save the cell to a GDS file
gdspy.write_gds('oval.gds', cell=cell)