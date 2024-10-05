import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("circle_cell")

# Create a circle on layer 0 with a radius of 10 mm, centered at (0, 0)
circle = gdspy.Round((0, 0), 10, layer=0, number_of_points=100)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds("circle.gds")