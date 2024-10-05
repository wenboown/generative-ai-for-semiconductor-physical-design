import gdspy

# Step 1: Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Step 2: Define the layers
via_layer = lib.new_layer(1, 'via', color=(255, 255, 0))  # yellow
metal_layer = lib.new_layer(2, 'metal', color=(0, 0, 255))  # blue
pad_layer = lib.new_layer(3, 'pad', color=(255, 0, 0))  # red

# Step 3: Define the via and pad radius
via_radius = 10
pad_radius = 30

# Step 4: Define the metal connection width and length
metal_width = 40
metal_length = 600

# Step 5: Define the positions of the vias
via1_pos = (50, 150)
via2_pos = (550, 150)

# Step 6: Calculate the metal connection coordinates
metal_x1 = via1_pos[0] - 50
metal_x2 = via2_pos[0] + 50
metal_y1 = via1_pos[1] - metal_width / 2
metal_y2 = via1_pos[1] + metal_width / 2

# Step 7: Create the vias, pads, and metal connection
via1 = gdspy.Round(
    via1_pos,
    via_radius,
    number_of_points=32,
    layer=via_layer
)
via2 = gdspy.Round(
    via2_pos,
    via_radius,
    number_of_points=32,
    layer=via_layer
)
pad1 = gdspy.Round(
    via1_pos,
    pad_radius,
    number_of_points=32,
    layer=pad_layer
)
pad2 = gdspy.Round(
    via2_pos,
    pad_radius,
    number_of_points=32,
    layer=pad_layer
)
metal = gdspy.Rectangle(
    (metal_x1, metal_y1),
    (metal_x2, metal_y2),
    layer=metal_layer
)

# Step 8: Add the elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(pad1)
cell.add(pad2)
cell.add(metal)

# Step 9: Save the design to a GDS file
lib.write_gds('design.gds')