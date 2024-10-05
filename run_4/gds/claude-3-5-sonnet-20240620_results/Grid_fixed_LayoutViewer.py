import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID')

# Define grid parameters
layer = 1
datatype = 4
grid_spacing = 5000  # 5 µm in nanometers
width = 200000  # 200 µm in nanometers
height = 400000  # 400 µm in nanometers
origin = (100, 800)  # in nanometers

# Create vertical lines
for x in range(0, width + 1, grid_spacing):
    points = [
        (origin[0] + x, origin[1]),
        (origin[0] + x, origin[1] + height)
    ]
    path = gdspy.Path(1, points[0])
    path.segment(height, '+y', layer=layer, datatype=datatype)
    cell.add(path)

# Create horizontal lines
for y in range(0, height + 1, grid_spacing):
    points = [
        (origin[0], origin[1] + y),
        (origin[0] + width, origin[1] + y)
    ]
    path = gdspy.Path(1, points[0])
    path.segment(width, '+x', layer=layer, datatype=datatype)
    cell.add(path)

# Save the layout to a GDSII file
lib.write_gds('grid_layout.gds')

# Optional: View the layout