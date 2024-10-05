import gdspy

# Define GDSII library
lib = gdspy.GdsLibrary()

# Define the name of the cell
cell_name = "GRID_CELL"
cell = lib.new_cell(cell_name)

# Layer and datatype for the grid lines
layer = 1
datatype = 4

# Grid specifications
grid_spacing = 5 # in micrometers
total_width = 200 # in micrometers
total_height = 400 # in micrometers

# Convert grid spacing, width, and height to nanometers
grid_spacing_nm = grid_spacing * 1000
total_width_nm = total_width * 1000
total_height_nm = total_height * 1000

# Origin coordinates
origin_x = 100
origin_y = 800

# Draw vertical grid lines
x = origin_x
while x <= origin_x + total_width_nm:
    line = gdspy.Path(1, (x, origin_y))
    line.segment(total_height_nm, '+y', layer=layer, datatype=datatype)
    cell.add(line)
    x += grid_spacing_nm
    
# Draw horizontal grid lines
y = origin_y
while y <= origin_y + total_height_nm:
    line = gdspy.Path(1, (origin_x, y))
    line.segment(total_width_nm, '+x', layer=layer, datatype=datatype)
    cell.add(line)
    y += grid_spacing_nm

# Save the library in a GDSII file
gds_filename = 'grid_layout.gds'
lib.write_gds(gds_filename)

print(f"GDSII file '{gds_filename}' successfully generated.")