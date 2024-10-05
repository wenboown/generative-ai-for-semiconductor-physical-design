import gdspy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('LAYOUT')

# Active regions (layer 1)
active1 = gdspy.Rectangle((0, 0), (20, 5), layer=1)
active2 = gdspy.Rectangle((25, 0), (45, 5), layer=1)
active3 = gdspy.Rectangle((50, 0), (70, 5), layer=1)
cell.add([active1, active2, active3])

# Polysilicon gate pattern (grid-like structure with widths of 0.5 µm) on layer 2
vertical_lines = []
for x in range(0, 71, 5):  # x from 0 to 70 inclusive, step 5 µm
    line = gdspy.Rectangle((x - 0.25, -5), (x + 0.25, 10), layer=2)
    vertical_lines.append(line)
cell.add(vertical_lines)

horizontal_lines = []
for y in range(-5, 11, 5):  # y from -5 to 10 inclusive, step 5 µm
    line = gdspy.Rectangle((0, y - 0.25), (70, y + 0.25), layer=2)
    horizontal_lines.append(line)
cell.add(horizontal_lines)

# Contact holes (1 µm x 1 µm) at intersections on layer 3
x_positions = [x for x in range(0, 71, 5)]  # Vertical lines positions
y_positions = [0, 5]  # Only positions within active regions

# Function to check if x is within any active region
def in_active_region(x):
    active_regions = [(0, 20), (25, 45), (50, 70)]
    for x_min, x_max in active_regions:
        if x >= x_min and x <= x_max:
            return True
    return False

# Positions where contacts should be placed
contact_positions = [(x, y) for x in x_positions if in_active_region(x) for y in y_positions]

# Create contact holes
contact_holes = []
for x, y in contact_positions:
    contact = gdspy.Rectangle((x - 0.5, y - 0.5), (x + 0.5, y + 0.5), layer=3)
    contact_holes.append(contact)
cell.add(contact_holes)

# Write the design to a GDS file
lib.write_gds('layout.gds')