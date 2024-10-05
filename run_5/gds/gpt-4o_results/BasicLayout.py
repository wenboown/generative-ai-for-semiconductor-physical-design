import gdspy

# Create a library and a new cell named "example_layout"
lib = gdspy.GdsLibrary()
cell = lib.new_cell('example_layout')

# Define layer numbers and datatypes (optional)
layer_active = 1
layer_poly = 2
layer_contact = 3

# Define dimensions
active_width = 10e-6  # 10 micrometers
active_height = 5e-6  # 5 micrometers
poly_width = 1e-6     # 1 micrometer
contact_size = 1e-6   # 1 micrometer

# Coordinates for the active region (bottom-left corner)
active_x0 = 0
active_y0 = 0

# Active region: Rectangle with bottom-left corner at (0, 0)
active_region = gdspy.Rectangle(
    (active_x0, active_y0),
    (active_x0 + active_width, active_y0 + active_height),
    layer=layer_active
)

# Add the active region to the cell
cell.add(active_region)

# Coordinates for the polysilicon gate (center of active region, vertically)
poly_x0 = active_x0 + (active_width - poly_width) / 2
poly_y0 = active_y0
poly_y1 = active_y0 + active_height

# Polysilicon gate: Rectangle with width 1 µm, crossing vertically at the center
poly_gate = gdspy.Rectangle(
    (poly_x0, poly_y0),
    (poly_x0 + poly_width, poly_y1),
    layer=layer_poly
)

# Add the polysilicon gate to the cell
cell.add(poly_gate)

# Coordinates for the contact holes
contact_x_spacing = poly_width + 1e-6   # 1 µm spacing from the poly gate
contact1_x0 = poly_x0 - contact_x_spacing - contact_size
contact2_x0 = poly_x0 + poly_width + contact_x_spacing

# Contact holes: Two squares of size 1 µm x 1 µm, 1 µm away from the gate
contact1 = gdspy.Rectangle(
    (contact1_x0, active_y0 + (active_height - contact_size) / 2),
    (contact1_x0 + contact_size, active_y0 + (active_height + contact_size) / 2),
    layer=layer_contact
)

contact2 = gdspy.Rectangle(
    (contact2_x0, active_y0 + (active_height - contact_size) / 2),
    (contact2_x0 + contact_size, active_y0 + (active_height + contact_size) / 2),
    layer=layer_contact
)

# Add the contact holes to the cell
cell.add(contact1)
cell.add(contact2)

# Save the GDS layout to a file
lib.write_gds('example_layout.gds')

print("GDS layout has been created and saved as 'example_layout.gds'")