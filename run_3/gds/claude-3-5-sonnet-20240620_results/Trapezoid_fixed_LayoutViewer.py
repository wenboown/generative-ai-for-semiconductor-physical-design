import gdspy
import numpy as np

# Convert mm to µm (GDS units are typically in µm)
scale = 1000

# Calculate trapezoid dimensions in µm
upper_edge = 10 * scale
lower_edge = 20 * scale
height = 8 * scale

# Calculate half-widths for centering
upper_half_width = upper_edge / 2
lower_half_width = lower_edge / 2

# Calculate trapezoid vertices
vertices = [
    (-lower_half_width, -height/2),
    (lower_half_width, -height/2),
    (upper_half_width, height/2),
    (-upper_half_width, height/2)
]

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRAPEZOID')

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(vertices, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the library to a GDS file
lib.write_gds('trapezoid.gds')

print("Trapezoid GDS file has been generated: trapezoid.gds")

# Optionally, view the layout