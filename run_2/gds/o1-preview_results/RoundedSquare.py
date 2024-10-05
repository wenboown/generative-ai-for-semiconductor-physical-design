import gdspy
import numpy as np

# Define the unit and precision for the layout (using millimeters).
lib = gdspy.GdsLibrary(unit=1e-3)  # Units are in mm

# Create a new cell for the design.
cell = lib.new_cell('ROUNDED_SQUARE')

# Define the dimensions and corner radius.
width = 10.0     # Width of the square in mm
height = 10.0    # Height of the square in mm
radius = 1.0     # Corner radius in mm

# Number of points to approximate each quarter-circle arc.
num_pts = 16

# Begin constructing the points for the polygon.

# Start from the bottom-left corner (after the corner rounding).
points_x = []
points_y = []

# Bottom edge (from left to right).
points_x.extend(np.linspace(radius, width - radius, num=2, endpoint=False))
points_y.extend([0, 0])

# Bottom-right corner arc.
theta = np.linspace(-0.5 * np.pi, 0, num=num_pts)
points_x.extend((width - radius) + radius * np.cos(theta))
points_y.extend(radius + radius * np.sin(theta))

# Right edge (from bottom to top).
points_x.extend([width, width])
points_y.extend(np.linspace(radius, height - radius, num=2, endpoint=False))

# Top-right corner arc.
theta = np.linspace(0, 0.5 * np.pi, num=num_pts)
points_x.extend((width - radius) + radius * np.cos(theta))
points_y.extend((height - radius) + radius * np.sin(theta))

# Top edge (from right to left).
points_x.extend(np.linspace(width - radius, radius, num=2, endpoint=False))
points_y.extend([height, height])

# Top-left corner arc.
theta = np.linspace(0.5 * np.pi, np.pi, num=num_pts)
points_x.extend(radius + radius * np.cos(theta))
points_y.extend((height - radius) + radius * np.sin(theta))

# Left edge (from top to bottom).
points_x.extend([0, 0])
points_y.extend(np.linspace(height - radius, radius, num=2, endpoint=False))

# Bottom-left corner arc.
theta = np.linspace(np.pi, 1.5 * np.pi, num=num_pts)
points_x.extend(radius + radius * np.cos(theta))
points_y.extend(radius + radius * np.sin(theta))

# Close the polygon by connecting back to the starting point.
polygon_points = list(zip(points_x, points_y))

# Create the polygon representing the rounded square.
rounded_square = gdspy.Polygon(polygon_points)

# Add the rounded square to the cell.
cell.add(rounded_square)

# Save the design to a GDSII file.
lib.write_gds('rounded_square.gds')