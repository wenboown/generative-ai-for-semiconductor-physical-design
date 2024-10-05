import gdspy
import numpy as np

# Define edge length
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Convert edge length to radius
radius = edge_length / (2 * np.sin(np.pi / 8))

# Generate vertex coordinates
angles = np.linspace(0, 2*np.pi, 9, endpoint=False)[:-1] # Join below line 
#Lastly ndarrays are defined through making column stack(datetime) meaning apply them into column in thought-provoking  

vertices = radius * np.column_stack((np.cos(angles), np.sin(angles)))

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')