import gdspy

# Create a GDSII library and a cell
library = gdspy.GdsLibrary()
cell = library.new_cell('CELL')

# Define layers
ACTIVE_LAYER = 1
POLY_LAYER = 2
CONTACT_LAYER = 3

# Draw three rectangular active regions (20 µm x 5 µm) with 5 µm spacing
# First active region
rect1 = gdspy.Rectangle((0, 0), (20, 5), layer=ACTIVE_LAYER)
cell.add(rect1)

# Second active region, 5 µm spacing from the first
rect2 = gdspy.Rectangle((25, 0), (45, 5), layer=ACTIVE_LAYER)
cell.add(rect2)

# Third active region, 5 µm spacing from the second
rect3 = gdspy.Rectangle((50, 0), (70, 5), layer=ACTIVE_LAYER)
cell.add(rect3)

# Create polysilicon gate pattern (grid-like structure with 0.5 µm width lines)
# Vertical lines from x = 0 µm to x = 75 µm with 5 µm spacing
x_positions = list(range(0, 76, 5))
for x in x_positions:
    x1 = x - 0.25  # Shift by half the line width to center the line
    x2 = x + 0.25
    vertical_line = gdspy.Rectangle((x1, 0), (x2, 15), layer=POLY_LAYER)
    cell.add(vertical_line)

# Horizontal lines from y = 0 µm to y = 15 µm with 5 µm spacing
y_positions = [0, 5, 10, 15]
for y in y_positions:
    y1 = y - 0.25
    y2 = y + 0.25
    horizontal_line = gdspy.Rectangle((0, y1), (75, y2), layer=POLY_LAYER)
    cell.add(horizontal_line)

# Add contact holes (1 µm x 1 µm) at intersections of polysilicon grid and active regions
contact_size = 1.0  # Size of the contact holes

# Active region boundaries
active_regions = [
    {'x_start': 0, 'x_end': 20},
    {'x_start': 25, 'x_end': 45},
    {'x_start': 50, 'x_end': 70}
]

# Loop through each active region
for region in active_regions:
    x_active_start = region['x_start']
    x_active_end = region['x_end']
    # Find vertical grid lines within the active region
    x_contacts = [x for x in x_positions if (x >= x_active_start - 0.25) and (x <= x_active_end + 0.25)]
    # Horizontal grid lines intersecting active regions (y from 0 µm to 5 µm)
    y_contacts = [y for y in y_positions if y >= 0 and y <= 5]
    # Create contact holes at the intersections
    for x in x_contacts:
        for y in y_contacts:
            contact = gdspy.Rectangle(
                (x - contact_size / 2, y - contact_size / 2),
                (x + contact_size / 2, y + contact_size / 2),
                layer=CONTACT_LAYER
            )
            cell.add(contact)

# Save the design to a GDSII file
library.write_gds('layout.gds')