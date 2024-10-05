import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layers
via_layer = {'layer': 0, 'datatype': 0}  # yellow
metal_layer = {'layer': 1, 'datatype': 0}  # blue
pad_layer = {'layer': 2, 'datatype': 0}  # red

# Define the geometric elements
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
via1_center = (50, 150)
via2_center = (550, 150)
metal_margin = 10
via_metal_space = 50

# Create the vias
via1 = gdspy.Round(via1_center, via_radius, **via_layer)
via2 = gdspy.Round(via2_center, via_radius, **via_layer)

# Create the pads
pad1 = gdspy.Round(via1_center, pad_radius, **pad_layer)
pad2 = gdspy.Round(via2_center, pad_radius, **pad_layer)

# Create the metal connection
metal_path = gdspy.Path(metal_width, (via1_center[0] - via_metal_space, via1_center[1]), **metal_layer)
metal_path.segment((via2_center[0] + via_metal_space, via2_center[1]))

# Add the elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(pad1)
cell.add(pad2)
cell.add(metal_path)

# Save the design to a GDS file
lib.write_gds('design.gds')