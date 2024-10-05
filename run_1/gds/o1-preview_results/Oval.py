import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to add shapes
cell = lib.new_cell('OVAL_CELL')

# Define the center of the oval
center = (0, 0)  # in microns

# Define the radii for the oval (half of the major and minor axes)
radius_x = 10e3  # Half of 20 mm in microns (10 mm * 1000)
radius_y = 6.5e3  # Half of 13 mm in microns (6.5 mm * 1000)

# Create the oval (ellipse)
oval = gdspy.Ellipse(center, radius=(radius_x, radius_y), layer=0)

# Add the oval to the cell
cell.add(oval)

# Save the library to a GDSII file
lib.write_gds('oval.gds')