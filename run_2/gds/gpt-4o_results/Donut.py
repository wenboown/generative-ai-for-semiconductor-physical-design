import gdspy

# Define the outer radius, inner radius, and max distance between points
outer_radius = 10.0  # in mm
inner_radius = 5.0   # in mm
max_points_distance = 0.01  # in mm

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Define the outer circle
outer_circle = gdspy.Round((0, 0), outer_radius, tolerance=max_points_distance)

# Define the inner circle (as a polygon with zero thickness)
inner_circle = gdspy.Round((0, 0), inner_radius, tolerance=max_points_distance)

# Subtract inner circle from the outer circle to create a donut shape
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the library to a GDSII file
lib.write_gds('donut.gds')

print("Donut shape generated successfully in 'donut.gds'")