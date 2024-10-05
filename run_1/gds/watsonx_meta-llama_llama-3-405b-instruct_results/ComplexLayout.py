import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layer numbers for active, polysilicon, and contact
active_layer = 1
poly_layer = 2
contact_layer = 3

# Draw three rectangular active regions
active_width = 20
active_height = 5
active_spacing = 5

active_rect1 = gdspy.Rectangle((0, 0), (active_width, active_height), layer=active_layer)
active_rect2 = gdspy.Rectangle((active_width + active_spacing, 0), (2*active_width + active_spacing, active_height), layer=active_layer)
active_rect3 = gdspy.Rectangle((2*active_width + 2*active_spacing, 0), (3*active_width + 2*active_spacing, active_height), layer=active_layer)

cell.add(active_rect1)
cell.add(active_rect2)
cell.add(active_rect3)

# Create a complex polysilicon gate pattern
poly_width = 0.5

for i in range(10):
    hline = gdspy.Rectangle((0, i*5), (3*active_width + 2*active_spacing, i*5 + poly_width), layer=poly_layer)
    cell.add(hline)

for i in range(7):
    vline = gdspy.Rectangle((i*(active_width//2 + active_spacing//2), 0), (i*(active_width//2 + active_spacing//2) + poly_width, 50), layer=poly_layer)
    cell.add(vline)

# Add contact holes
contact_size = 1
for i in range(10):
    for j in range(3):
        x = j*(active_width + active_spacing) + active_width//2
        y = i*5
        contact = gdspy.Rectangle((x - contact_size//2, y - contact_size//2), (x + contact_size//2, y + contact_size//2), layer=contact_layer)
        cell.add(contact)

# Save the design to a GDS file
lib.write_gds('design.gds')