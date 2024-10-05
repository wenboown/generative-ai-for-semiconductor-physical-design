import gdspy

# Define the GDSII library and cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell("TRAPEZOID")

# Trapezoid specifications in mm, convert to microns (µm)
upper_edge = 10.0 * 1000  # Convert mm to µm
lower_edge = 20.0 * 1000  # Convert mm to µm
height = 8.0 * 1000       # Convert mm to µm

# Center coordinates
center_x = 0.0
center_y = 0.0

# Calculate half dimensions
half_upper = upper_edge / 2.0
half_lower = lower_edge / 2.0
half_height = height / 2.0

# Define the vertices of the trapezoid
vertices = [
    (center_x - half_upper, center_y + half_height),  # Upper left
    (center_x + half_upper, center_y + half_height),  # Upper right
    (center_x + half_lower, center_y - half_height),  # Lower right
    (center_x - half_lower, center_y - half_height)   # Lower left
]

# Create the polygon for the trapezoid
trapezoid = gdspy.Polygon(vertices, layer=0)

# Add the polygon to the GDSII cell
cell.add(trapezoid)

# Save the library to a GDSII file
gdsii_lib.write_gds('trapezoid.gds')

print("Trapezoid GDS layout generated successfully.")