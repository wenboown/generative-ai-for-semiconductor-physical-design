import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Create a circle with radius 10 mm (10,000 μm) centered at (0, 0)
circle = gdspy.Round((0, 0), 10000, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the library to a GDS file
lib.write_gds('circle.gds')

print("GDS file 'circle.gds' has been created.")