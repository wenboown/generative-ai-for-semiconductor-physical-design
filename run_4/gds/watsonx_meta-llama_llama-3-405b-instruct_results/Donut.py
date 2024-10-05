import gdspy
import numpy as np

# Define the design requirements
outer_radius = 10  # mm
inner_radius = 5  # mm
max_distance = 0.01  # mm

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Generate the donut shape
theta = np.linspace(0, 2*np.pi, int(2*np.pi*outer_radius/max_distance))
outer_x = outer_radius * np.cos(theta)
outer_y = outer_radius * np.sin(theta)

inner_x = inner_radius * np.cos(theta)
inner_y = inner_radius * np.sin(theta)

# Create the outer and inner polygons
outer_polygon = gdspy.Polygon([(x, y) for x, y in zip(outer_x, outer_y)])
inner_polygon = gdspy.Polygon([(x, y) for x, y in zip(inner_x, inner_y)])

# Subtract the inner polygon from the outer polygon to create the donut shape
donut_polygon = gdspy.fast_boolean(outer_polygon, inner_polygon, 'not', precision=0.001)

# Add the donut shape to the cell
cell.add(donut_polygon)

# Save the design to a GDS file
lib.write_gds('donut.gds')