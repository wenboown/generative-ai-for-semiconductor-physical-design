import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Layer definitions
layer_active = 1
layer_poly = 2
layer_contact = 3

# Active region dimensions
active_width = 20
active_height = 5
active_spacing = 5

# Create active regions
for i in range(3):
    x = i * (active_width + active_spacing)
    rectangle = gdspy.Rectangle((x, 0), (x + active_width, active_height), layer=layer_active)
    cell.add(rectangle)

# Polysilicon gate pattern
poly_width = 0.5
grid_pitch_x = 5
grid_pitch_y = 5
total_width = 3 * active_width + 2 * active_spacing
total_height = active_height

# Vertical lines
for x in np.arange(0, total_width + grid_pitch_x, grid_pitch_x):
    line = gdspy.Rectangle((x - poly_width/2, -2), (x + poly_width/2, total_height + 2), layer=layer_poly)
    cell.add(line)

# Horizontal lines
for y in np.arange(0, total_height + grid_pitch_y, grid_pitch_y):
    line = gdspy.Rectangle((-2, y - poly_width/2), (total_width + 2, y + poly_width/2), layer=layer_poly)
    cell.add(line)

# Contact holes
contact_size = 1
for i in range(3):
    active_x = i * (active_width + active_spacing)
    for x in np.arange(active_x, active_x + active_width + grid_pitch_x, grid_pitch_x):
        for y in np.arange(0, active_height + grid_pitch_y, grid_pitch_y):
            if active_x <= x <= active_x + active_width:
                contact = gdspy.Rectangle(
                    (x - contact_size/2, y - contact_size/2),
                    (x + contact_size/2, y + contact_size/2),
                    layer=layer_contact
                )
                cell.add(contact)

# Save the layout to a GDSII file
lib.write_gds('layout.gds')

# Display all cells using the internal viewer