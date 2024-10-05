import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRAPEZOID')

# Define the trapezoid vertices
vertices = [
    (-5e6, 4e6),   # Top left
    (5e6, 4e6),    # Top right
    (10e6, -4e6),  # Bottom right
    (-10e6, -4e6)  # Bottom left
]

# Create a polygon for the trapezoid
trapezoid = gdspy.Polygon(vertices, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')

# Optional: View the layout