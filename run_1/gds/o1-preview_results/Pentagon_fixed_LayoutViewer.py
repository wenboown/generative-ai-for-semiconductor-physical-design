import gdspy
import numpy as np

# Define the side length (s) in mm
side_length = 10.0  # mm

# Calculate the radius (R) of the circumscribed circle
R = side_length / (2 * np.sin(np.pi / 5))

# Calculate the starting angle (theta_0)
# This ensures the pentagon is centered at (0,0)
theta_0 = np.pi / 2  # 90 degrees, so one vertex points upwards

# Calculate vertex angles theta_n
angles = np.array([2 * np.pi * n / 5 + theta_0 for n in range(5)])

# Calculate the coordinates of the vertices
x_vertices = R * np.cos(angles)
y_vertices = R * np.sin(angles)
vertices = [(x, y) for x, y in zip(x_vertices, y_vertices)]

# Validate side lengths (optional)
# for i in range(5):
#     x0, y0 = vertices[i]
#     x1, y1 = vertices[(i + 1) % 5]
#     side = np.hypot(x1 - x0, y1 - y0)
#     assert np.isclose(side, side_length), f"Side {i} length error: {side}"

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Create the pentagon polygon and add it to the cell
pentagon = gdspy.Polygon(vertices, layer=1)
cell.add(pentagon)

# Save the layout to a GDSII file
lib.write_gds('pentagon.gds')

# Optional: View the layout (uncomment the next line to display the layout)