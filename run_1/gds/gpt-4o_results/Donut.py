import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the design will be placed
cell = lib.new_cell('DONUT')

# Define parameters for the donut shape
outer_radius = 10.0   # Outer radius in mm
inner_radius = 5.0    # Inner radius in mm
max_points_distance = 0.01  # Maximum distance between points in mm

# Create the outer and inner circles 
outer_circle = gdspy.Round((0, 0), outer_radius, tolerance=max_points_distance)
inner_circle = gdspy.Round((0, 0), inner_radius, tolerance=max_points_distance)

# Subtract the inner circle from the outer circle to create a donut shape
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the layout to a GDS file
lib.write_gds('donut_design.gds')

print("Donut shape GDS layout created successfully.")