import gdspy
import numpy as np

# Define dimensions in microns
width = 10000  # 10 mm
height = 10000  # 10 mm
corner_radius = 1000  # 1 mm

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ROUNDED_SQUARE')

# Function to create a rounded rectangle (square in this case)
def rounded_rectangle(x0, y0, x1, y1, r):
    from math import pi
    # Ensure the radius is not larger than half the width or height
    r = min(r, abs(x1 - x0) / 2, abs(y1 - y0) / 2)
    # Number of points for each corner arc
    n = 50
    theta = np.linspace(0, 0.5 * pi, n)
    # Corner center coordinates
    corners = [
        (x1 - r, y1 - r),  # Top-right
        (x0 + r, y1 - r),  # Top-left
        (x0 + r, y0 + r),  # Bottom-left
        (x1 - r, y0 + r),  # Bottom-right
    ]
    # Build the rounded corners
    points = []
    for i, (cx, cy) in enumerate(corners):
        angles = theta + i * 0.5 * pi
        x = cx + r * np.cos(angles)
        y = cy + r * np.sin(angles)
        points.append(np.column_stack([x, y]))
    # Concatenate all points
    polygon_points = np.concatenate(points)
    return polygon_points

# Generate the rounded square polygon
points = rounded_rectangle(0, 0, width, height, corner_radius)
polygon = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(polygon)

# Save the GDS file
lib.write_gds('rounded_square.gds')