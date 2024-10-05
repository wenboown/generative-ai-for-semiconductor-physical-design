import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell("TRAPEZOID")

# Convert mm to µm (GDS uses µm as its unit)
scale = 1000

# Calculate the coordinates of the trapezoid
upper_half_width = 5 * scale
lower_half_width = 10 * scale
half_height = 4 * scale

# Define the points of the trapezoid
points = [
    (-lower_half_width, -half_height),
    (-upper_half_width, half_height),
    (upper_half_width, half_height),
    (lower_half_width, -half_height)
]

# Create a polygon for the trapezoid
trapezoid = gdspy.Polygon(points, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds("trapezoid.gds")

# Optional: View the layout