import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Define the active region as a rectangle
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=0, datatype=0)
cell.add(active_region)

# Define the polysilicon gate as a rectangle
gate = gdspy.Rectangle((4.5, 0), (5.5, 5), layer=1, datatype=0)
cell.add(gate)

# Define the contact holes as squares
contact_hole1 = gdspy.Rectangle((3, 2), (4, 3), layer=2, datatype=0)
contact_hole2 = gdspy.Rectangle((6, 2), (7, 3), layer=2, datatype=0)
cell.add(contact_hole1)
cell.add(contact_hole2)

# Save the design to a GDS file
lib.write_gds('layout.gds')