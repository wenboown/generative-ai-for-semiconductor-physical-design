import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Create the circle
# Note: gdspy uses nanometers as the default unit, so we need to convert mm to nm
radius_nm = 10 * 1e6  # 10 mm = 10,000,000 nm
circle = gdspy.Round((0, 0), radius_nm, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')

print("GDS file 'circle.gds' has been generated successfully.")