import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Donut Shape")

# Define the outer and inner radii
outer_radius = 10  # mm
inner_radius = 5  # mm

# Define the max distance between points for a smoother circle
max_dist = 0.01  # mm

# Create the outer circle
outer_circle = gdspy.Circle((0, 0), outer_radius, max_points=360, layer=0)

# Create the inner circle
inner_circle = gdspy.Circle((0, 0), inner_radius, max_points=360, layer=0)

# Subtract the inner circle from the outer circle to create the donut shape
donut_shape = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut_shape)

# Save the design to a GDS file
lib.write_gds("donut_shape.gds")