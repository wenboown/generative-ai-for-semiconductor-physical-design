import gdspy

# Define the GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('LAYOUT')

# Dimensions for the active regions
active_width = 20
active_height = 5

# Spacing between active regions
spacing = 5

# Define active regions
active_regions = []
for i in range(3):
    x_offset = i * (active_width + spacing)
    rect = gdspy.Rectangle((x_offset, 0), (x_offset + active_width, active_height))
    active_regions.append(rect)
    cell.add(rect)

# Dimensions for the polysilicon gate pattern
poly_width = 0.5
poly_spacing = 2  # Spacing between polysilicon lines

# Define polysilicon gate pattern grid
poly_lines = []
x = 0
while x <= (2*(active_width + spacing)):
    rect = gdspy.Rectangle((x, -poly_width), (x + poly_width, 2*active_height + spacing))
    poly_lines.append(rect)
    cell.add(rect)
    x += poly_spacing + poly_width

y = -poly_width
while y <= (2*(active_height + spacing)):
    rect = gdspy.Rectangle((-poly_width, y), (2*(active_width + spacing), y + poly_width))
    poly_lines.append(rect)
    cell.add(rect)
    y += poly_spacing + poly_width

# Dimensions for contact holes
contact_size = 1

# Adding contact holes at the intersections of polysilicon gate pattern and active regions
contact_holes = []
for i in range(3):
    for j, x in enumerate(range(0, 2*(active_width + spacing), poly_spacing + poly_width)):
        for y in range(0, 2*(active_height + spacing), poly_spacing + poly_width):
            x_offset = i * (active_width + spacing)
            if x_offset <= x < x_offset + active_width and 0 <= y < active_height:
                contact = gdspy.Rectangle((x - contact_size*0.5, y - contact_size*0.5), 
                                           (x + contact_size*0.5, y + contact_size*0.5))
                contact_holes.append(contact)
                cell.add(contact)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')