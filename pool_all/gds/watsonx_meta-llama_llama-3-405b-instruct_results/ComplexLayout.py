import gdspy

# Define units for the layout (e.g., micrometers)
unit = 1.0e-6
precision = 1.0e-9

# Create a new GDS library
lib = gdspy.GdsLibrary(unit=unit, precision=precision)

# Create a new cell in the library
cell = lib.new_cell('LAYOUT')

# Define the active region dimensions
active_width = 20.0
active_height = 5.0
spacing = 5.0

# Draw three rectangular active regions
for i in range(3):
    x_offset = i * (active_width + spacing)
    active_region = gdspy.Rectangle((x_offset, 0), 
                                    (x_offset + active_width, active_height))
    cell.add(active_region)

# Define the polysilicon gate pattern dimensions and properties
poly_line_width = 0.5
grid_spacing = 5.0

# Calculate the grid boundaries based on active regions
x_max = 3 * (active_width + spacing) - spacing
y_max = active_height

# Create vertical polysilicon gate lines
x_start = -grid_spacing
while x_start < x_max + grid_spacing:
    poly_vertical = gdspy.Rectangle((x_start, -grid_spacing),
                                    (x_start + poly_line_width, y_max + grid_spacing))
    cell.add(poly_vertical)
    x_start += grid_spacing

# Create horizontal polysilicon gate lines
y_start = -grid_spacing
while y_start < y_max + grid_spacing:
    poly_horizontal = gdspy.Rectangle((0, y_start),
                                      (x_max, y_start + poly_line_width))
    cell.add(poly_horizontal)
    y_start += grid_spacing

# Define contact hole dimensions
contact_width = 1.0
contact_height = 1.0

# Add contact holes at the intersections of the polysilicon gate pattern and active regions
for i in range(3):
    x_offset = i * (active_width + spacing)
    for j in range(5):
        contact_x = x_offset + j * grid_spacing
        for k in range(int(y_max // grid_spacing) + 1):
            contact_y = k * grid_spacing
            contact_hole = gdspy.Rectangle((contact_x - contact_width / 2,
                                            contact_y - contact_height / 2),
                                           (contact_x + contact_width / 2,
                                            contact_y + contact_height / 2))
            cell.add(contact_hole)

# Write the layout to a GDS file
lib.write_gds('layout.gds')

print("GDS layout generated and saved to 'layout.gds'.")