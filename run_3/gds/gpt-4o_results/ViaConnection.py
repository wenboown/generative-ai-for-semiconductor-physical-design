import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell
cell = lib.new_cell('DESIGN_CELL')

# Dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
margin = 10
space_between_vias_and_metal = 50

# Positions
via_position1 = (50, 150)
via_position2 = (550, 150)

# Layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Create vias
via1 = gdspy.Round(via_position1, via_radius, layer=via_layer)
via2 = gdspy.Round(via_position2, via_radius, layer=via_layer)

# Create pads
pad1 = gdspy.Round(via_position1, pad_radius, layer=pad_layer)
pad2 = gdspy.Round(via_position2, pad_radius, layer=pad_layer)

# Calculate metal connection coordinates, ensuring spacing
metal_x1 = via_position1[0] - space_between_vias_and_metal
metal_x2 = via_position2[0] + space_between_vias_and_metal
metal_y1 = via_position1[1] - metal_width / 2
metal_y2 = via_position1[1] + metal_width / 2

metal_connection = gdspy.Rectangle(
    (metal_x1, metal_y1), (metal_x2, metal_y2), layer=metal_layer
)

# Add shapes to cell
cell.add(via1)
cell.add(via2)
cell.add(pad1)
cell.add(pad2)
cell.add(metal_connection)

# Write out the GDS file
lib.write_gds('layout_design.gds')