import gdspy

# Define the GDSII file
gdsii = False  # Use GDSII instead of GDSII-XR

# Parse the user's design specifications
radius = 10e3  # Convert 10 mm to microns
center = (0, 0)

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle')

# Create a circle with precise coordinates
circle = gdspy.Round(center, radius, layer=0, datatype=0)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds', unit=1.0e-6, precision=1.0e-9)