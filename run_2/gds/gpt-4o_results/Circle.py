import gdspy

# Define the layer and datatype
layer = 0
datatype = 0

# Define the circle parameters
radius = 10000  # in microns (10 mm = 10000 microns)
center = (0, 0)

# Create a new GDSII library
gdsii_lib = gdspy.GdsLibrary()

# Create a new cell
cell = gdsii_lib.new_cell('CIRCLE_CELL')

# Create the circle
circle = gdspy.Round(center, radius, tolerance=1e-3, layer=layer, datatype=datatype)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
gdsii_lib.write_gds('circle_design.gds')

print("GDSII file 'circle_design.gds' created successfully.")