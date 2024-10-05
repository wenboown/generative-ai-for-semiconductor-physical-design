import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OVAL')

# Define the parameters for the oval
major_axis = 20000  # 20 mm in nanometers
minor_axis = 13000  # 13 mm in nanometers
center = (0, 0)
layer = 0

# Create the oval using gdspy.Round
# We use 64 points to approximate the ellipse, which should be sufficient for most purposes
oval = gdspy.Round(
    center,
    major_axis / 2,  # x-radius
    number_of_points=64,
    major_axis=major_axis,
    minor_axis=minor_axis,
    layer=layer
)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been generated.")