import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Draw three rectangular active regions
active_region_width = 20
active_region_height = 5
active_region_spacing = 5

for i in range(3):
    x = i * (active_region_width + active_region_spacing)
    y = 0
    rect = gdspy.Rectangle((x, y), (x + active_region_width, y + active_region_height))
    cell.add(rect)

# Create a complex polysilicon gate pattern
poly_width = 0.5
poly_end_x = 60  # arbitrary end x-coordinate for demonstration purposes

for x in [5, 15, 25, 35, 45, 55]:
    for y in [0, 2, 4, 6, 8]:
        if x < poly_end_x:
            line = gdspy.Rectangle((x, y), (x + poly_width, y + poly_width))
            cell.add(line)
            line = gdspy.Rectangle((x, y + 2), (x + 4, y + 2 + poly_width))
            cell.add(line)
            line = gdspy.Rectangle((x + 2, y), (x + 2 + poly_width, y + 4))
            cell.add(line)

# Add several contact holes
contact_size = 1

for x in [5, 25, 45]:
    for y in [2, 6]:
        contact = gdspy.Rectangle((x, y), (x + contact_size, y + contact_size))
        cell.add(contact)

# Save the design to a GDS file
lib.write_gds('layout.gds')