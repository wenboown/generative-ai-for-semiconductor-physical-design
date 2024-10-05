import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Define the layers
via_layer = lib.new_layer(0, 'via')
metal_layer = lib.new_layer(1, 'metal')
pad_layer = lib.new_layer(2, 'pad')

# Define the via radius, pad radius, and metal connection width
via_radius = 10
pad_radius = 30
metal_width = 40

# Define the position of the vias
via1_pos = (50, 150)
via2_pos = (550, 150)

# Calculate the metal connection length and margin
metal_length = via2_pos[0] - via1_pos[0] + 2 * (via_radius + 50)
metal_margin = 10

# Create the vias
via1 = gdspy.Round(via1_pos, via_radius, layer=via_layer)
via2 = gdspy.Round(via2_pos, via_radius, layer=via_layer)
cell.add(via1)
cell.add(via2)

# Create the metal connection
metal = gdspy.Rectangle((via1_pos[0] - 50, via1_pos[1] - metal_width/2), 
                        (via2_pos[0] + 50, via2_pos[1] + metal_width/2), 
                        layer=metal_layer)
cell.add(metal)

# Create the pads
pad1 = gdspy.Round((via1_pos[0] - (pad_radius + metal_margin), via1_pos[1]), 
                   pad_radius, layer=pad_layer)
pad2 = gdspy.Round((via2_pos[0] + (pad_radius + metal_margin), via2_pos[1]), 
                   pad_radius, layer=pad_layer)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('layout.gds')