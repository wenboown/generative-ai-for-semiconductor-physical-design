import gdspy
import string

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# 1. Create the 3.2 mm circle
circle = gdspy.Round((0, 0), 1600)  # Radius is half of 3200 µm
cell.add(circle)

# 2. Create the "+" sign fiducial mark
def create_fiducial(size=50):
    vertical = gdspy.Rectangle((-size/10, -size/2), (size/10, size/2))
    horizontal = gdspy.Rectangle((-size/2, -size/10), (size/2, size/10))
    return gdspy.boolean(vertical, horizontal, 'or')

fiducial = create_fiducial()

# 3. Place fiducial marks in a grid pattern
grid_size = 200  # 200 µm apart
rows = 26  # A to Z
cols = int(3200 / grid_size)  # Number of columns that fit in the circle

for i in range(-rows//2, rows//2 + 1):
    for j in range(-cols//2, cols//2 + 1):
        x = j * grid_size
        y = i * grid_size
        if x**2 + y**2 <= 1600**2:  # Check if inside the circle
            cell.add(gdspy.CellReference(fiducial, (x, y)))
            
            # 4. Add annotations
            row_label = string.ascii_uppercase[i + rows//2]
            col_label = str(j + cols//2 + 1)
            label = f"{row_label}{col_label}"
            
            text = gdspy.Text(label, 40, (x + 30, y - 30))
            cell.add(text)

# Save the design to a GDS file
lib.write_gds('fiducial_circle.gds')

# Display all cells using the internal viewer