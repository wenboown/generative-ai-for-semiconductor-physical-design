import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_WITH_ROUNDED_CORNERS')

# Define the square dimensions (in micrometers)
width = 10000  # 10 mm = 10000 µm
height = 10000  # 10 mm = 10000 µm

# Define the corner radius (in micrometers)
radius = 1000  # 1 mm = 1000 µm

# Create rounded corners
corner_topleft = gdspy.Round((radius, height - radius), radius, number_of_points=128,
                             initial_angle=np.pi, final_angle=3*np.pi/2)
corner_topright = gdspy.Round((width - radius, height - radius), radius, number_of_points=128,
                              initial_angle=3*np.pi/2, final_angle=2*np.pi)
corner_bottomright = gdspy.Round((width - radius, radius), radius, number_of_points=128,
                                 initial_angle=0, final_angle=np.pi/2)
corner_bottomleft = gdspy.Round((radius, radius), radius, number_of_points=128,
                                initial_angle=np.pi/2, final_angle=np.pi)

# Create straight edges
edge_top = gdspy.Rectangle((radius, height - radius), (width - radius, height))
edge_right = gdspy.Rectangle((width - radius, radius), (width, height - radius))
edge_bottom = gdspy.Rectangle((radius, 0), (width - radius, radius))
edge_left = gdspy.Rectangle((0, radius), (radius, height - radius))

# Combine all elements
square_with_rounded_corners = gdspy.boolean(
    [corner_topleft, corner_topright, corner_bottomright, corner_bottomleft,
     edge_top, edge_right, edge_bottom, edge_left],
    None, 'or'
)

# Add the combined shape to the cell
cell.add(square_with_rounded_corners)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')

# Optionally, view the layout