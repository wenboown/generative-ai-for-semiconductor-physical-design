import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layers
via_layer = {'layer': 0, 'datatype': 0}  # yellow
metal_layer = {'layer': 1, 'datatype': 0}  # blue
pad_layer = {'layer': 2, 'datatype': 0}  # red

# Create the vias
via1 = gdspy.Round((50, 150), 10, **via_layer)
via2 = gdspy.Round((550, 150), 10, **via_layer)

# Create the pads
pad1 = gdspy.Round((50, 150), 30, **pad_layer)
pad2 = gdspy.Round((550, 150), 30, **pad_layer)

# Create the metal connection
metal = gdspy.Rectangle((0, 140), (600, 160), **metal_layer)

# Add the shapes to the cell
cell.add([via1, via2, pad1, pad2, metal])

# Save the design to a GDS file
lib.write_gds('design.gds')