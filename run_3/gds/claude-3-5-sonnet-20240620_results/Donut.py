import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Set the unit to millimeters (1000 units = 1 mm)
unit = 1000

# Define the parameters
outer_radius = 10 * unit  # 10 mm
inner_radius = 5 * unit   # 5 mm
max_distance = 0.01 * unit  # 0.01 mm between points

# Calculate the number of points needed for smooth circles
num_points = int(np.ceil(2 * np.pi * outer_radius / max_distance))

# Generate points for the outer circle
t = np.linspace(0, 2*np.pi, num_points, endpoint=False)
outer_circle = np.column_stack((outer_radius * np.cos(t), outer_radius * np.sin(t)))

# Generate points for the inner circle
inner_circle = np.column_stack((inner_radius * np.cos(t), inner_radius * np.sin(t)))

# Create a polygon for the donut shape
donut = gdspy.Polygon(outer_circle, layer=0)
donut.holes([inner_circle])

# Add the donut to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')

print("Donut shape has been generated and saved as 'donut.gds'")