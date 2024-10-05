import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Convert 10 mm to microns (1 mm = 1000 microns)
radius_microns = 10 * 1000

# Create a circle
circle = gdspy.Round((0, 0), radius_microns, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been generated.")