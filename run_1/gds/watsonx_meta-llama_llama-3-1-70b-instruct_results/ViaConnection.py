import gdspy

# Define the GDS layer numbers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Create a new GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell('layout')

# Define the via radius, pad radius, and metal connection width
via_radius = 10
pad_radius = 30
metal_width = 40

# Calculate the metal connection length
metal_length = 600

# Calculate the x-coordinate for the metal connection
metal_x1 = 50 - 50
metal_x2 = 550 + 50

# Create the vias
via1 = gdspy.Round((50, 150), via_radius, via_layer)
via2 = gdspy.Round((550, 150), via_radius, via_layer)
cell.add(via1)
cell.add(via2)

# Create the pads
pad1 = gdspy.Round((50, 150), pad_radius, pad_layer)
pad2 = gdspy.Round((550, 150), pad_radius, pad_layer)
cell.add(pad1)
cell.add(pad2)

# Create the metal connection
metal = gdspy.Rectangle((metal_x1, 150 - metal_width/2), (metal_x2, 150 + metal_width/2), metal_layer)
cell.add(metal)

# Save the design to a GDS file
lib.write_gds('layout.gds')