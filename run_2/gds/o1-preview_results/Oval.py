import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('OVAL_CELL')

# Define the center of the oval (ellipse)
center = (0, 0)

# Convert dimensions from millimeters to microns (1 mm = 1000 microns)
major_axis_length_mm = 20  # in millimeters
minor_axis_length_mm = 13  # in millimeters
major_axis_length = major_axis_length_mm * 1000  # in microns
minor_axis_length = minor_axis_length_mm * 1000  # in microns

# Calculate the radii of the ellipse (half of the axis lengths)
x_radius = major_axis_length / 2  # Radius along the x-axis
y_radius = minor_axis_length / 2  # Radius along the y-axis

# Create the oval using gdspy.Round with specified radii
oval = gdspy.Round(
    center,
    radius=(x_radius, y_radius),
    inner_radius=0,
    initial_angle=0,
    final_angle=2 * np.pi,
    tolerance=0.001,
    layer=0
)

# Add the oval to the cell
cell.add(oval)

# Save the library in a GDSII file
lib.write_gds('oval.gds')