import gdspy
import numpy as np

# Convert mm to microns
major_axis = 20 * 1000  # 20 mm to microns
minor_axis = 13 * 1000  # 13 mm to microns

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OVAL')

# Create the oval (ellipse)
oval = gdspy.Round(
    (0, 0),  # Center point
    major_axis / 2,  # X radius
    minor_axis / 2,  # Y radius
    layer=0,
    number_of_points=128  # Increase for smoother curve
)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

# Optional: View the layout