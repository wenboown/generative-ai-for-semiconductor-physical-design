import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary(unit=1)
cell = lib.new_cell('design')

# Define the layers
via_layer = {'layer': 0, 'datatype': 0}  # yellow
metal_layer = {'layer': 1, 'datatype': 0}  # blue
pad_layer = {'layer': 2, 'datatype': 0}  # red

# Define the via radius, pad radius, and metal connection width
via_radius = 10
pad_radius = 30
metal_width = 40

# Define the coordinates for the vias and metal connection
via1_center = (50, 150)
via2_center = (550, 150)
metal_length = 600

# Create the vias
via1 = gdspy.Round(via1_center, via_radius, layer=via_layer['layer'], datatype=via_layer['datatype'])
via2 = gdspy.Round(via2_center, via_radius, layer=via_layer['layer'], datatype=via_layer['datatype'])

# Create the metal connection
metal_points = [(via1_center[0] - metal_width / 2 - 50, via1_center[1]), 
                (via1_center[0] + metal_width / 2 + 50, via1_center[1]), 
                (via2_center[0] + metal_width / 2 + 50, via2_center[1]), 
                (via2_center[0] - metal_width / 2 - 50, via2_center[1])]
metal = gdspy.FlexPath(metal_points, metal_width, layer=metal_layer['layer'], datatype=metal_layer['datatype'])

# Create the pads
pad1 = gdspy.Round(via1_center, pad_radius, layer=pad_layer['layer'], datatype=pad_layer['datatype'])
pad2 = gdspy.Round(via2_center, pad_radius, layer=pad_layer['layer'], datatype=pad_layer['datatype'])

# Add the elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('design.gds')