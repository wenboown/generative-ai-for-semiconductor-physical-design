import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
height = 5  # mm
center = (0, 0)  # coordinates in mm
layer = 1

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-9)  # unit: 1 um, precision: 1 nm
cell = lib.new_cell('hello_gds')

# Create the text element with precise coordinates
font = gdspy TribeFont(name='default', size=height*0.6)
text_path = gdspy.Text(text, center, size=height, layer=layer, font=font)
cell.add(text_path)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')