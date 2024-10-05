import gdspy

# Define the layers
via_layer = {"layer": 1, "datatype": 0}
metal_layer = {"layer": 2, "datatype": 0}
pad_layer = {"layer": 3, "datatype": 0}

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Create a new cell for the layout
cell = lib.new_cell("Layout")

# Define the via radius, pad radius, and metal connection width
via_radius = 10
pad_radius = 30
metal_width = 40

# Define the positions of the vias
via1_position = (50, 150)
via2_position = (550, 150)

# Define the metal connection length
metal_length = 600

# Create the vias
via1 = gdspy.Round(via1_position, via_radius, **via_layer)
via2 = gdspy.Round(via2_position, via_radius, **via_layer)

# Add the vias to the cell
cell.add(via1)
cell.add(via2)

# Create the pads
pad1 = gdspy.Round(via1_position, pad_radius, **pad_layer)
pad2 = gdspy.Round(via2_position, pad_radius, **pad_layer)

# Add the pads to the cell
cell.add(pad1)
cell.add(pad2)

# Calculate the metal connection coordinates
metal_x1 = via1_position[0] - 50
metal_x2 = via2_position[0] + 50
metal_y1 = via1_position[1] - metal_width / 2
metal_y2 = via1_position[1] + metal_width / 2

# Create the metal connection
metal = gdspy.Rectangle((metal_x1, metal_y1), (metal_x2, metal_y2), **metal_layer)

# Add the metal connection to the cell
cell.add(metal)

# Save the design to a GDS file
lib.write_gds("layout.gds")