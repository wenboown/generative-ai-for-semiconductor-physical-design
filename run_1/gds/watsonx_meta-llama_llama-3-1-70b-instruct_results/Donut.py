import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Donut")

# Define the parameters
outer_radius = 10  # mm
inner_radius = 5   # mm
max_distance = 0.01  # mm

# Create the outer circle
outer_circle = gdspy.Circle(center=(0, 0), radius=outer_radius, number_of_points=round(2*3.14159*outer_radius/max_distance))

# Create the inner circle
inner_circle = gdspy.Circle(center=(0, 0), radius=inner_radius, number_of_points=round(2*3.14159*inner_radius/max_distance))

# Subtract the inner circle from the outer circle to create the donut shape
donut = gdspy.Polygon.outer(outer_circle).polygon - gdspy.Polygon.outer(inner_circle).polygon

# Add the donut shape to the cell
cell.add(donut)

# Save the GDS file
lib.write_gds("donut.gds")