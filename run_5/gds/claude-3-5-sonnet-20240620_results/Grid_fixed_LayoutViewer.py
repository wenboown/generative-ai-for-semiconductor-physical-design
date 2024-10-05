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
origin = (100, 800)  # Origin coordinates in nanometers

# Create horizontal lines
for y in range(0, height + grid_spacing, grid_spacing):
    start = (origin[0], origin[1] + y)
    end = (origin[0] + width, origin[1] + y)
    cell.add(gdspy.Path(1, start).segment(width, '+x', layer=layer, datatype=datatype))

# Create vertical lines
for x in range(0, width + grid_spacing, grid_spacing):
    start = (origin[0] + x, origin[1])
    end = (origin[0] + x, origin[1] + height)
    cell.add(gdspy.Path(1, start).segment(height, '+y', layer=layer, datatype=datatype))

# Save the layout to a GDSII file
lib.write_gds('grid_layout.gds')

# Optional: View the layout